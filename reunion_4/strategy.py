"""
Patrón Strategy
Descripción: Define una familia de algoritmos intercambiables
"""

from abc import ABC, abstractmethod

# Interfaz abstracta para las estrategias de pago
class EstrategiaPago(ABC):
    """Interfaz abstracta que define el contrato para todas las estrategias de pago"""

    @abstractmethod
    def procesar_pago(self, monto):
        pass

# Implementaciones concretas de estrategias de pago
class PagoTarjeta(EstrategiaPago):
    """Estrategia concreta para procesar pagos con tarjeta de crédito"""

    def procesar_pago(self, monto):
        return f"Procesando ${monto} con tarjeta 💳"

class PagoEfectivo(EstrategiaPago):
    """Estrategia concreta para procesar pagos en efectivo"""

    def procesar_pago(self, monto):
        return f"Procesando ${monto} en efectivo 💵"

# Contexto que utiliza las estrategias
class ProcesadorPagos:
    """
    Contexto que maneja el procesamiento de pagos usando diferentes estrategias
    """

    def __init__(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def ejecutar_pago(self, monto):
        return self._estrategia.procesar_pago(monto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un procesador con estrategia de tarjeta
    procesador = ProcesadorPagos(PagoTarjeta())
    print(procesador.ejecutar_pago(100))  # Output: Procesando $100 con tarjeta 💳

    # Cambiar dinámicamente a estrategia de efectivo
    procesador.cambiar_estrategia(PagoEfectivo())
    print(procesador.ejecutar_pago(50))   # Output: Procesando $50 en efectivo 💵

    # Demostrar flexibilidad: cambiar de vuelta a tarjeta
    procesador.cambiar_estrategia(PagoTarjeta())
    print(procesador.ejecutar_pago(75))   # Output: Procesando $75 con tarjeta 💳
