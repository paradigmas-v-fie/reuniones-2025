class Refugio:  # Clase que gestiona el refugio de mascotas
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
