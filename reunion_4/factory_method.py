"""
Patrón Factory Method
Descripción: Creación de objetos sin especificar la clase exacta
"""

from abc import ABC, abstractmethod

# Clase abstracta base para vehículos
class Vehiculo(ABC):

    @abstractmethod
    def acelerar(self):
        pass

# Implementaciones concretas de vehículos
class Auto(Vehiculo):

    def acelerar(self):
        return "Auto acelerando 🚗"

class Moto(Vehiculo):

    def acelerar(self):
        return "Moto acelerando 🏍️"

# Factory para crear vehículos
class FabricaVehiculos:

    @staticmethod
    def crear_vehiculo(tipo):
        vehiculos = {
            "auto": Auto,
            "moto": Moto
        }

        clase_vehiculo = vehiculos.get(tipo)
        if clase_vehiculo:
            return clase_vehiculo()
        raise ValueError(f"Tipo de vehículo '{tipo}' no válido")

# Ejemplo de uso
if __name__ == "__main__":
    vehiculo = FabricaVehiculos.crear_vehiculo("auto")
    print(vehiculo.acelerar())  # Output: Auto acelerando 🚗

    vehiculo = FabricaVehiculos.crear_vehiculo("moto")
    print(vehiculo.acelerar())  # Output: Moto acelerando 🏍️
