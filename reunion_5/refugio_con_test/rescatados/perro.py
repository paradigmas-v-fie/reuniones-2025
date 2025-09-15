from datetime import datetime, timedelta
from .mascota import Mascota

class Perro(Mascota):  # Clase que representa un perro en el refugio
    def cumplir_maximo(self, mascotas):
        cantidad = sum(1 for m in mascotas if isinstance(m, Perro))
        return cantidad < 3

    def esta_rehabilitada(self):
        return (datetime.now() - self.fecha_ingreso) >= timedelta(days=30)
