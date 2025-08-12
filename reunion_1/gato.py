from mascota import Mascota


class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre)

    def saludar(self):
        super().saludar()
        print(f"miau!")
