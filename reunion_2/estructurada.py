"""
Atencion! Esto no es POO
Este ejemplo muestra como se ve un programa utilizando el paradigma estructurado.
El uso de dataclass en Python permite simplificar la creacion de estructuras que emulen
los struct de otros lenguajes.
"""
from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    anio: int

@dataclass
class Socio:
    nombre: str
    libros_prestados: list

def agregar_libro(biblioteca: list, libro: Libro):
    biblioteca.append(libro)

def prestar_libro(biblioteca: list, socio: Socio, libro: Libro):
    if libro in biblioteca:
        biblioteca.remove(libro)
        socio.libros_prestados.append(libro)
        return True
    return False

def devolver_libro(biblioteca: list, socio: Socio, libro: Libro):
    if libro in socio.libros_prestados:
        socio.libros_prestados.remove(libro)
        biblioteca.append(libro)
        return True
    return False

def mostrar_biblioteca(biblioteca: list):
    print("Libros disponibles:")
    for i, libro in enumerate(biblioteca):
        print(f"{i + 1}. {libro.titulo} - {libro.autor} ({libro.anio})")

def mostrar_libros_socio(socio: Socio):
    print(f"Libros de {socio.nombre}:")
    for libro in socio.libros_prestados:
        print(f"  {libro.titulo} - {libro.autor}")


def main():
    biblioteca = []

    libro_1 = Libro(titulo="Cien años de soledad", autor="Gabriel García Márquez", anio=1967)
    libro_2 = Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", anio=1605)
    libro_3 = Libro(titulo="El Aleph", autor="Jorge Luis Borges", anio=1945)


    agregar_libro(biblioteca, libro_1)
    agregar_libro(biblioteca, libro_2)
    agregar_libro(biblioteca, libro_3)

    mostrar_biblioteca(biblioteca)

    socio_1 = Socio(nombre="Carlos", libros_prestados=[])
    socio_2 = Socio(nombre="Ana", libros_prestados=[])
    socio_3 = Socio(nombre="Luis", libros_prestados=[])

    prestar_libro(biblioteca, socio_1, libro_1)
    prestar_libro(biblioteca, socio_2, libro_2)

    mostrar_biblioteca(biblioteca)

    mostrar_libros_socio(socio_1)
    mostrar_libros_socio(socio_2)
    mostrar_libros_socio(socio_3)

if __name__ == "__main__":
    main()
