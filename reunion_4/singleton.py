"""
Patrón Singleton
Descripción: Garantiza una única instancia de la clase
"""

class ConfiguracionSistema:
    """
    Clase Singleton que maneja la configuración del sistema.
    Solo permite una instancia única durante toda la ejecución.
    """

    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.configuracion = {}  # Inicializa el diccionario de configuración
        return cls._instancia

    def __init__(self):
        print("init")

    def set_config(self, clave, valor):
        self.configuracion[clave] = valor

    def get_config(self, clave):
        return self.configuracion.get(clave)

# Ejemplo de uso y verificación
if __name__ == "__main__":
    # Creamos múltiples referencias
    config1 = ConfiguracionSistema()
    config2 = ConfiguracionSistema()

    # Establecemos configuraciones desde diferentes referencias
    config1.set_config("api_url", "https://api.ejemplo.com")
    config2.set_config("timeout", 30)

    # Verificamos que ambas referencias apuntan al mismo objeto
    print(f"config1 timeout: {config1.get_config('timeout')}")  # Output: 30
    print(f"config2 api_url: {config2.get_config('api_url')}")  # Output: https://api.ejemplo.com

    # Verificaciones de que son la misma instancia
    print(f"¿Son el mismo objeto? {config1 is config2}")  # Output: True
    print(f"¿Tienen el mismo ID? {id(config1) == id(config2)}")  # Output: True

    # Mostrar todas las configuraciones
    print(f"Configuración completa: {config1.configuracion}")
