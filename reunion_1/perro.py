from mascota import Mascota


class Perro(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)

    def saludar(self):
        super().saludar()
        print("guau!")
