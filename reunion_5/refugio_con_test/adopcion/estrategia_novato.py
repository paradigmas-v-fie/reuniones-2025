class EstrategiaNovato():  # Estrategia para adoptantes novatos
    def puede_adoptar(self, adoptante, _):
        return len(adoptante.mascotas) == 0
