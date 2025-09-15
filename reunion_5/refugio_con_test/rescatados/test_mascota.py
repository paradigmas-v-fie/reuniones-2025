import unittest
from datetime import datetime
from .mascota import Mascota

class TestMascota(unittest.TestCase):
    def setUp(self):
        # Crear una clase concreta para la prueba
        class MascotaConcreta(Mascota):
            def cumplir_maximo(self) -> bool:
                # Implementación mínima - devuelve la respuesta válida más simple
                return False

            def esta_rehabilitada(self) -> bool:
                # Implementación mínima - devuelve la respuesta válida más simple
                return False

        self.mascota = MascotaConcreta("Firulais", 1, datetime.now())

    def tearDown(self):
        self.mascota = None

    def test_init_mascota(self):
        self.assertEqual(self.mascota.apodo, "Firulais")
        self.assertEqual(self.mascota.id_mascota, 1)
        self.assertIsInstance(self.mascota.fecha_ingreso, datetime)

    def test_saludar_no_rehabilitada(self):
        result = self.mascota.saludar()
        self.assertEqual(result, "Firulais aún no está listo para saludar.")

    def test_saludar_rehabilitada(self):
        # Rehabilitar la mascota, cambiando la funcion esta_rehabilitada
        self.mascota.esta_rehabilitada = lambda: True
        result = self.mascota.saludar()
        self.assertEqual(result, 'Firulais te saluda con cariño.')
