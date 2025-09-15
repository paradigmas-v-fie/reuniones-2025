class Fecha:
    DIAS_MESES = [31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self, dia, mes, anio):
        self._anio = anio
        self.set_mes(mes)
        self.set_dia(dia)


    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_anio(self):
        return self._anio

    def set_dia(self, dia):
        if dia < 1:
            raise ValueError("Dia invalido")
        if Fecha.DIAS_MESES[self.get_mes() - 1] < dia:
            raise ValueError("Dia invalido")
        self._dia = dia

    def set_mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mes invalido")
        self._mes = mes

    def _es_bisiesto(self):
        anio = self._anio
        return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


