class EstrategiaComun():  # Estrategia común de adopción
    def puede_adoptar(self, adoptante, mascota):
        return mascota.cumplir_maximo(adoptante.mascotas)
