import uuid
from typing import List, Optional

from app.users.domain import Usuario


class Modificador:
    def aplicar_precio(self, precio_actual: float, usuario: Optional[Usuario]) -> float:
        return precio_actual

    def etiqueta_fragment(self) -> str:
        return ""  # No se muestra en la etiqueta


class RecargoFijo(Modificador):
    def __init__(self, recargo):
        self.recargo = recargo

    def aplicar_precio(self, precio_actual, usuario: Optional[Usuario]):
        return precio_actual + self.recargo


class IVA(Modificador):
    PORCENTAJE = 0.21
    taxfree = False

    def __init__(self, taxfree=False):
        self.taxfree = taxfree

    def aplicar_precio(self, precio_actual, usuario: Optional[Usuario]):
        if self.taxfree and usuario and usuario.extranjero:
            return precio_actual
        else:
            return round(precio_actual * (1 + self.PORCENTAJE), 2)

    def etiqueta_fragment(self) -> str:
        if self.taxfree:
            return "Tax-Free"
        else:
            return ""


class Pesado(Modificador):
    def aplicar_precio(self, precio_actual: float, usuario: Optional[Usuario]) -> float:
        return precio_actual + 3000.0

    def etiqueta_fragment(self) -> str:
        return "PESADO"


class Promocion(Modificador):
    def __init__(self, descuento: float):
        self.descuento = descuento

    def etiqueta_fragment(self) -> str:
        return f"PROMO {int(self.descuento)}%"

    def aplicar_precio(self, precio_actual: float, usuario: Optional[Usuario]) -> float:
        return round(precio_actual * (1 - self.descuento / 100.0), 2)


class Producto:
    def __init__(
        self,
        nombre: str,
        precio_base: float,
        iva: IVA,
        modificadores: List[Modificador] = [],
    ):
        self.nombre = nombre
        self.precio_base = precio_base
        self.modificadores = [iva] + modificadores
        # Agregamos un id (UUIDv4) para poder operar con los productos sin depender del nombre
        self.id = uuid.uuid4()
        # https://es.wikipedia.org/wiki/Identificador_%C3%BAnico_universal#UUID_Versi%C3%B3n_4_(al_azar)

    def puede_comprar(self, usuario: Usuario) -> bool:
        return True

    def precio_final(self, usuario: Optional[Usuario]) -> float:
        total = self.precio_base
        for m in reversed(self.modificadores):
            total = m.aplicar_precio(total, usuario)
        return total

    def etiqueta(self, nombre_cliente):
        fragmentos = []
        for m in self.modificadores:
            fragmentos.append(m.etiqueta_fragment())
        advertencias = " - " + ", ".join(fragmentos) if fragmentos else ""
        return f"Para {nombre_cliente}: {self.nombre}{advertencias}"


class ProductoRegulado(Producto):
    def __init__(self, nombre, precio_base, edad_minima, iva, modificadores=[]):
        self.edad_minima = edad_minima
        super().__init__(
            nombre=nombre, precio_base=precio_base, iva=iva, modificadores=modificadores
        )

    def puede_comprar(self, usuario: Usuario):
        return usuario.edad >= self.edad_minima
