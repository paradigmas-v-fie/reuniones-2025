from .mascota import Mascota

class Ave(Mascota):  # Clase que representa un ave en el refugio
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Ave))
        return cantidad < 10

    def esta_rehabilitada(self):
        return True
