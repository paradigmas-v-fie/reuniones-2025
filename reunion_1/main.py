from gato import Gato
from perro import Perro
from mascota import Mascota


class Araña:
    def saludar(self):
        print("Pica!")


def main():
    refugio = []

    refugio.append(Gato("Pepe"))
    refugio.append(Perro("Chola"))
    refugio.append(Gato("Hector"))
    refugio.append(Araña())

    print(refugio)

    # Mascota m;
    for m in refugio:
        m.saludar()


if __name__ == "__main__":
    main()
