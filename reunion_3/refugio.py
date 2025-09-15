from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, apodo, id_mascota, fecha_ingreso):
        self.apodo = apodo
        self.id_mascota = id_mascota
        self.fecha_ingreso = fecha_ingreso

    @property
    def disponible_para_adopcion(self):
        return self.esta_rehabilitada()

    def saludar(self):
        if self.esta_rehabilitada():
            return f"{self.apodo} te saluda con cariño."
        else:
            return f"{self.apodo} aún no está listo para saludar."

    @abstractmethod
    def cumplir_maximo(self, mascotas):
        pass

    @abstractmethod
    def esta_rehabilitada(self):
        pass


class Perro(Mascota):
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Perro))
        return cantidad < 3

    def esta_rehabilitada(self):
        return (datetime.now() - self.fecha_ingreso) >= timedelta(days=30)

class Gato(Mascota):
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Gato))
        return cantidad < 5

    def esta_rehabilitada(self):
        return (datetime.now() - self.fecha_ingreso) >= timedelta(days=180)

class Ave(Mascota):
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Ave))
        return cantidad < 10

    def esta_rehabilitada(self):
        return True

# Estrategias de adopción
class EstrategiaComun():
    def puede_adoptar(self, adoptante, mascota):
        return mascota.cumplir_maximo(adoptante.mascotas)

class EstrategiaNovato():
    def puede_adoptar(self, adoptante, _):
        return len(adoptante.mascotas) == 0

class EstrategiaTransito(EstrategiaComun):
    def puede_adoptar(self, adoptante, mascota):
        puede = super().puede_adoptar(adoptante, mascota)
        for m in adoptante.mascotas:
            if type(m) != type(mascota):
                puede = False
        return puede

class Adoptante:
    def __init__(self, nombre, estrategia):
        self.mascotas = []
        self.nombre = nombre
        self.estrategia = estrategia

    def adoptar(self, mascota):
        if self.estrategia.puede_adoptar(self, mascota):
            self.mascotas.append(mascota)
        else:
            raise ValueError(f"{self.nombre} no cumple las condiciones para adoptar a {mascota.apodo}!")


class Refugio:
    def __init__(self):
        self.mascotas = []
        self.adopciones = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_mascotas_disponibles(self):
        return [m for m in self.mascotas if m.disponible_para_adopcion]

    def registrar_adopcion(self, adoptante, mascota):
        if mascota in self.listar_mascotas_disponibles():
            adoptante.adoptar(mascota)  # Lanza excepción si no se puede adoptar
            self.adopciones.append((adoptante, mascota))
            self.mascotas.remove(mascota)
        else:
            raise ValueError(f"{mascota.apodo} no está disponible para adopcion!")

    def historial_adopciones(self):
        return self.adopciones

def main():
    print("=== SISTEMA DE ADOPCIÓN DE MASCOTAS ===\n")

    # Crear refugio
    refugio = Refugio()

    # Crear mascotas con diferentes fechas de ingreso
    fecha_antigua = datetime.now() - timedelta(days=200)  # Rehabilitadas
    fecha_reciente = datetime.now() - timedelta(days=10)  # No rehabilitadas
    fecha_media = datetime.now() - timedelta(days=50)     # Solo perros rehabilitados

    # Mascotas rehabilitadas
    perro1 = Perro("Max", "P001", fecha_antigua)
    perro2 = Perro("Luna", "P002", fecha_media)
    gato1 = Gato("Miau", "G001", fecha_antigua)
    gato2 = Gato("Whiskers", "G002", fecha_antigua)
    ave1 = Ave("Piolín", "A001", fecha_reciente)  # Las aves siempre están rehabilitadas

    # Mascotas NO rehabilitadas
    perro_nuevo = Perro("Rocky", "P003", fecha_reciente)
    gato_nuevo = Gato("Shadow", "G003", fecha_reciente)

    # Agregar mascotas al refugio
    mascotas = [perro1, perro2, gato1, gato2, ave1, perro_nuevo, gato_nuevo]
    for mascota in mascotas:
        refugio.agregar_mascota(mascota)
        print(f"✓ {mascota.apodo} agregado al refugio - {mascota.saludar()}")

    print(f"\n--- MASCOTAS EN EL REFUGIO: {len(refugio.mascotas)} ---")
    disponibles = refugio.listar_mascotas_disponibles()
    print(f"--- MASCOTAS DISPONIBLES PARA ADOPCIÓN: {len(disponibles)} ---")
    for mascota in disponibles:
        print(f"  • {mascota.apodo} ({type(mascota).__name__})")

    # Crear adoptantes con diferentes estrategias
    adoptante_comun = Adoptante("Carlos", EstrategiaComun())
    adoptante_novato = Adoptante("María", EstrategiaNovato())
    adoptante_transito = Adoptante("Ana", EstrategiaTransito())

    print("\n=== PRUEBAS DE ADOPCIÓN ===\n")

    # Test 1: Adoptante común adopta un perro
    print("1. Adoptante común (Carlos) adopta a Max:")
    try:
        refugio.registrar_adopcion(adoptante_comun, perro1)
        print(f"   ✓ {perro1.apodo} adoptado por {adoptante_comun.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 2: Adoptante novato adopta un gato
    print("2. Adoptante novato (María) adopta a Miau:")
    try:
        refugio.registrar_adopcion(adoptante_novato, gato1)
        print(f"   ✓ {gato1.apodo} adoptado por {adoptante_novato.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 3: Adoptante tránsito adopta un ave
    print("3. Adoptante tránsito (Ana) adopta a Piolín:")
    try:
        refugio.registrar_adopcion(adoptante_transito, ave1)
        print(f"   ✓ {ave1.apodo} adoptado por {adoptante_transito.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 4: Adoptante novato intenta segunda adopción (debe fallar)
    print("4. Adoptante novato (María) intenta adoptar a Luna:")
    try:
        refugio.registrar_adopcion(adoptante_novato, perro2)
        print(f"   ✓ {perro2.apodo} adoptado por {adoptante_novato.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 5: Adoptante tránsito intenta adoptar diferente tipo (debe fallar)
    print("5. Adoptante tránsito (Ana) intenta adoptar a Whiskers (diferente tipo):")
    try:
        refugio.registrar_adopcion(adoptante_transito, gato2)
        print(f"   ✓ {gato2.apodo} adoptado por {adoptante_transito.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 6: Intentar adoptar mascota no rehabilitada
    print("6. Carlos intenta adoptar a Rocky (no rehabilitado):")
    try:
        refugio.registrar_adopcion(adoptante_comun, perro_nuevo)
        print(f"   ✓ {perro_nuevo.apodo} adoptado por {adoptante_comun.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 7: Adoptante común adopta más mascotas (hasta límite)
    print("7. Carlos adopta a Luna (segundo perro):")
    try:
        refugio.registrar_adopcion(adoptante_comun, perro2)
        print(f"   ✓ {perro2.apodo} adoptado por {adoptante_comun.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    # Test 8: Adoptante tránsito adopta mismo tipo
    print("8. Ana adopta otra ave (mismo tipo que ya tiene):")
    # Crear otra ave disponible
    ave2 = Ave("Canario", "A002", fecha_reciente)
    refugio.agregar_mascota(ave2)
    try:
        refugio.registrar_adopcion(adoptante_transito, ave2)
        print(f"   ✓ {ave2.apodo} adoptado por {adoptante_transito.nombre}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")

    print("\n=== ESTADO FINAL ===")

    print(f"\nMascotas en el refugio: {len(refugio.mascotas)}")
    for mascota in refugio.mascotas:
        estado = "Disponible" if mascota.disponible_para_adopcion else "En rehabilitación"
        print(f"  • {mascota.apodo} ({type(mascota).__name__}) - {estado}")

    print(f"\nTotal de adopciones realizadas: {len(refugio.historial_adopciones())}")
    for adoptante, mascota in refugio.historial_adopciones():
        print(f"  • {mascota.apodo} → {adoptante.nombre}")

    print(f"\nMascotas por adoptante:")
    for adoptante in [adoptante_comun, adoptante_novato, adoptante_transito]:
        print(f"  • {adoptante.nombre}: {len(adoptante.mascotas)} mascotas")
        for mascota in adoptante.mascotas:
            print(f"    - {mascota.apodo} ({type(mascota).__name__})")


if __name__ == "__main__":
    main()
