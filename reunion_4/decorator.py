"""
Patrón Decorator
Descripción: Añade funcionalidad dinámicamente a objetos
"""

# Clase base para el café
class Cafe:
    """Clase base que representa un café simple"""

    def costo(self):
        return 10

    def descripcion(self):
        return "Café base"

# Clase base para decoradores
class DecoradorCafe:
    """
    Clase base para todos los decoradores de café.
    Mantiene una referencia al objeto café que está siendo decorado.
    """

    def __init__(self, cafe):
        self._cafe = cafe

    def costo(self):
        return self._cafe.costo()

    def descripcion(self):
        return self._cafe.descripcion()

# Decoradores concretos
class ConLeche(DecoradorCafe):
    """Decorador que añade leche al café"""

    def costo(self):
        return self._cafe.costo() + 5

    def descripcion(self):
        return f"{self._cafe.descripcion()} + leche"

class ConChocolate(DecoradorCafe):
    """Decorador que añade chocolate al café"""

    def costo(self):
        return self._cafe.costo() + 8

    def descripcion(self):
        return f"{self._cafe.descripcion()} + chocolate"

class ConCrema(DecoradorCafe):
    """Decorador que añade crema al café"""

    def costo(self):
        return self._cafe.costo() + 3

    def descripcion(self):
        return f"{self._cafe.descripcion()} + crema"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un café base
    mi_cafe = Cafe()
    print(f"Café inicial: {mi_cafe.descripcion()} - ${mi_cafe.costo()}")

    # Añadir leche usando decorador
    mi_cafe = ConLeche(mi_cafe)
    print(f"Con leche: {mi_cafe.descripcion()} - ${mi_cafe.costo()}")

    # Añadir chocolate usando decorador
    mi_cafe = ConChocolate(mi_cafe)
    print(f"Con chocolate: {mi_cafe.descripcion()} - ${mi_cafe.costo()}")

    # Añadir crema usando decorador
    mi_cafe = ConCrema(mi_cafe)
    print(f"Con crema: {mi_cafe.descripcion()} - ${mi_cafe.costo()}")

    print("\n--- Ejemplo de composición diferente ---")

    # Crear otra combinación diferente
    cafe_especial = Cafe()
    cafe_especial = ConChocolate(cafe_especial)
    cafe_especial = ConChocolate(cafe_especial)  # Doble chocolate
    cafe_especial = ConLeche(cafe_especial)

    print(f"Café especial: {cafe_especial.descripcion()} - ${cafe_especial.costo()}")
