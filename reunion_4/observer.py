"""
Patrón Observer
Descripción: Notificación automática de cambios de estado
"""

# Clase Sujeto (Observable)
class Sujeto:
    """
    Clase que representa el sujeto observable.
    Mantiene una lista de observadores y les notifica cuando cambia su estado.
    """

    def __init__(self):
        """Inicializa el sujeto con una lista vacía de observadores"""
        self._observadores = []
        self._estado = None

    def agregar_observador(self, observador):
        """
        Agrega un observador a la lista
        Args:
            observador: Objeto observador que será notificado de cambios
        """
        self._observadores.append(observador)

    def remover_observador(self, observador):
        """
        Remueve un observador de la lista
        Args:
            observador: Objeto observador a remover
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self):
        """Notifica a todos los observadores sobre el cambio de estado"""
        for observador in self._observadores:
            observador.actualizar(self._estado)

    def cambiar_estado(self, estado):
        """
        Cambia el estado del sujeto y notifica a los observadores
        Args:
            estado: El nuevo estado del sujeto
        """
        self._estado = estado
        self.notificar()

    @property
    def estado(self):
        """Getter para el estado actual"""
        return self._estado

# Clase Observador Concreta
class ObservadorConcreto:
    """
    Implementación concreta de un observador.
    Recibe notificaciones cuando el sujeto cambia de estado.
    """

    def __init__(self, nombre):
        """
        Inicializa el observador con un nombre identificativo
        Args:
            nombre (str): Nombre del observador para identificarlo
        """
        self.nombre = nombre

    def actualizar(self, estado):
        """
        Método llamado cuando el sujeto notifica un cambio
        Args:
            estado: El nuevo estado del sujeto
        """
        print(f"{self.nombre} recibió: {estado}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear el sujeto observable
    sistema = Sujeto()

    # Crear observadores concretos
    monitor1 = ObservadorConcreto("Logger")
    monitor2 = ObservadorConcreto("Notificacion Whatsapp")
    monitor3 = ObservadorConcreto("Llamada telefonica")

    # Agregar observadores al sistema
    sistema.agregar_observador(monitor1)
    sistema.agregar_observador(monitor2)
    sistema.agregar_observador(monitor3)

    # Cambiar el estado - todos los observadores serán notificados
    sistema.cambiar_estado("ALERTA: CPU al 90%")
    print("---")

    # Cambiar estado nuevamente
    sistema.cambiar_estado("INFORMACIÓN: Sistema funcionando normalmente")
    print("---")

    # Remover un observador y cambiar estado
    sistema.remover_observador(monitor2)
    sistema.cambiar_estado("ADVERTENCIA: Memoria al 80%")
