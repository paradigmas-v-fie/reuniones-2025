# Niveles ---------------------------------------------------------------
class Nivel:
    def __init__(
        self, nombre, min_puntos, max_puntos, max_productos, saldo_negativo_max
    ):
        self.nombre = nombre
        self.min_puntos = min_puntos
        self.max_puntos = max_puntos
        self.max_productos = max_productos  # None = sin límite
        self.saldo_negativo_max = saldo_negativo_max

    def permite_agregar(self, cantidad_actual):
        if self.max_productos is None:
            return True
        return cantidad_actual < self.max_productos

    def permite_descubierto(self, saldo_final):
        return saldo_final >= self.saldo_negativo_max


# Instancias de niveles
NivelBronce = Nivel(
    nombre="Bronce",
    min_puntos=0,
    max_puntos=5000,
    max_productos=1,
    saldo_negativo_max=0,
)

NivelPlata = Nivel(
    nombre="Plata",
    min_puntos=5000,
    max_puntos=15000,
    max_productos=5,
    saldo_negativo_max=-5000,
)

NivelOro = Nivel(
    nombre="Oro",
    min_puntos=15000,
    max_puntos=float("inf"),
    max_productos=None,
    saldo_negativo_max=-20000,
)

# Lista ordenada de niveles
LEVELS = [NivelBronce, NivelPlata, NivelOro]


# Usuario ---------------------------------------------------------------
class Usuario:
    def __init__(self, nombre, edad, dinero, puntos=0, extranjero=False):
        self.nombre = nombre
        self.edad = edad
        self.dinero = dinero
        self.puntos = puntos
        self.carrito = []
        self.nivel = NivelBronce
        self.extranjero = extranjero

    def actualizar_nivel(self):
        for nivel in LEVELS:
            if nivel.min_puntos <= self.puntos < nivel.max_puntos:
                self.nivel = nivel
                break

    def agregar_producto(self, producto):
        if not producto.puede_comprar(self):
            raise Exception("No puede comprar este producto regulado!")
        if not self.nivel.permite_agregar(len(self.carrito)):
            raise Exception(
                f"Nivel {self.nivel.nombre} no permite agregar más productos al carrito"
            )
        self.carrito.append(producto)

    def cargar_dinero(self, monto):
        self.dinero += monto

    def total_carrito(self):
        if not self.carrito:
            return 0.0
        subtotal_productos = sum(p.precio_final(self) for p in self.carrito)
        return round(subtotal_productos, 2)

    def comprar(self):
        total = self.total_carrito()
        saldo_post = round(self.dinero - total, 2)
        if not self.nivel.permite_descubierto(saldo_post):
            raise Exception(
                "Saldo insuficiente para completar la compra según su nivel"
            )
        self.dinero = saldo_post
        puntos_ganados = int(round(total * 0.10))
        self.puntos += puntos_ganados
        self.carrito.clear()
        self.actualizar_nivel()
        return total
