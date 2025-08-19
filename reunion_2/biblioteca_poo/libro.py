class EstadoLibro:
    BUENO = "BUENO"
    ROTO = "ROTO"

class Libro:
    existentes = {} # Conjunto de tuplas (titulo, edicion, isbn)
    def __init__(self, titulo, edicion, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.edicion = edicion
        self.estado = EstadoLibro.BUENO
        self._validar(self)

    @classmethod
    def _validar(cls, libro):
        pass
        # Lanzar una excepcion si la combinacion titulo, edicion, isbn ya existe
        # y es difererente

    def __str__(self):
        return f"Titulo: {self.titulo} Edicion: {self.edicion} Isbn: {self.isbn}"


if __name__ == "__main__":
    libro = Libro("100 años de soledad", "1ra", "ABC123")
    libro_falso = Libro("100 años de soledad", "1ra", "DEF456")
