class Adoptante:  # Clase que representa un adoptante de mascotas
    def __init__(self, nombre, estrategia):
        self.mascotas = []
        self.nombre = nombre
        self.estrategia = estrategia

    def adoptar(self, mascota):
        if self.estrategia.puede_adoptar(self, mascota):
            self.mascotas.append(mascota)
        else:
            raise ValueError(f"{self.nombre} no cumple las condiciones para adoptar a {mascota.apodo}!")
