class Computadora:
    cantidad = 0

    @staticmethod
    def validar_memoria(memoria):
        if memoria in [4,8,16,32]:
            return memoria
        raise ValueError("Debe ser par")


    @classmethod
    def incrementar_cantidad(cls):
        cls.cantidad += 1

    @classmethod
    def decrementar_cantidad(cls):
        cls.cantidad -= 1

    def __init__(self):
        self.incrementar_cantidad()

    def __del__(self):
        self.decrementar_cantidad()



def main():
    print(Computadora.validar_memoria(8))
    mi_compu = Computadora()

    print(Computadora.cantidad)

    del mi_compu

    print(Computadora.cantidad)


if __name__ == "__main__":
    main()
