import pytest
from fecha import Fecha


class TestFecha:
    def testConstructor(self):
        fecha = Fecha(1, 1, 25)
        assert isinstance(fecha, Fecha) == True

    def testGetters(self):
        fecha = Fecha(12,5,87)
        assert fecha.get_dia() == 12
        assert fecha.get_mes() == 5
        assert fecha.get_anio() == 87

    def testDiaInvalido(self):
        with pytest.raises(ValueError, match="Dia invalido"):
            Fecha(0,3,2025)
        with pytest.raises(ValueError, match="Dia invalido"):
            Fecha(32,3,2025)

    def testMesInvalido(self):
        with pytest.raises(ValueError, match="Mes invalido"):
            Fecha(1,0,2025)
        with pytest.raises(ValueError, match="Mes invalido"):
            Fecha(1,13,2025)

    def testDiasAbril(self):
        with pytest.raises(ValueError, match="Dia invalido"):
            Fecha(31,4,2025)

    def testEsBisiesto(self):
        fecha = Fecha(30,4,2024)
        assert fecha._es_bisiesto() == True
