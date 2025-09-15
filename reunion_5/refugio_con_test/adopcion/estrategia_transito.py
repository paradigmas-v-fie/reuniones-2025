from .estrategia_comun import EstrategiaComun

class EstrategiaTransito(EstrategiaComun):  # Estrategia para adoptantes de tránsito
    def puede_adoptar(self, adoptante, mascota):
        puede = super().puede_adoptar(adoptante, mascota)
        for m in adoptante.mascotas:
            if type(m) != type(mascota):
                puede = False
        return puede
