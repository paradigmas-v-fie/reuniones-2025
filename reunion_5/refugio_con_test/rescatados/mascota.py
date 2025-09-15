from abc import ABC, abstractmethod

class Mascota(ABC):  # Clase abstracta base para todas las mascotas
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
