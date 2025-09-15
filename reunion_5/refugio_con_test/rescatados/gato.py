from datetime import datetime, timedelta
from .mascota import Mascota

class Gato(Mascota):  # Clase que representa un gato en el refugio
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Gato))
        return cantidad < 5

    def esta_rehabilitada(self):
        return (datetime.now() - self.fecha_ingreso) >= timedelta(days=180)
