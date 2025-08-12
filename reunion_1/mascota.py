class Mascota:
    def __init__(self, nombre):
        self.nombre = Mascota._validar_nombre(nombre)

    def saludar(self):
        print(f"{self.nombre} dice: ", end="")

    @staticmethod
    def _validar_nombre(nombre):
        """
        Este es un metodo estatico para validar el nombre
        del gato.
        """
        if not isinstance(nombre, str):
            raise TypeError("Debe ser cadena")
        if not nombre:
            raise ValueError("No puede ser vacio")
        return nombre  # El dato esta ok, retorno
