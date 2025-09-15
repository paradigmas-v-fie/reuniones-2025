import unittest
from datetime import datetime
from .ave import Ave

class TestAve(unittest.TestCase):
    def setUp(self):
        self.ave = Ave("Piolin", 2, datetime.now())

    def tearDown(self):
        self.ave = None

    def test_init_ave(self):
        self.assertEqual(self.ave.apodo, "Piolin")
        self.assertEqual(self.ave.id_mascota, 2)
        self.assertIsInstance(self.ave.fecha_ingreso, datetime)

    def test_rehabilitada_method(self):
        result = self.ave.esta_rehabilitada()
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
