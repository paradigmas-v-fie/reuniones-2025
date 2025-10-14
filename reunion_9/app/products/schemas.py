from pydantic import BaseModel
from .domain import ProductoRegulado, Producto

# Schema o DTO
class ProductCreateSchema(BaseModel):
    nombre: str
    precio_base: float
    regulado: bool = False

class ProductDetailSchema(BaseModel):
    nombre: str
    precio_base: float
    precio_final: float
    etiquetas: list[str] = []
    regulado: bool = False

    @staticmethod
    def from_domain(producto: Producto) -> "ProductDetailSchema":
        return ProductDetailSchema(
            nombre=producto.nombre,
            precio_base=producto.precio_base,
            precio_final=producto.precio_final(None),
            etiquetas=[
                mod.etiqueta_fragment() for mod in producto.modificadores if mod.etiqueta_fragment()
            ],
            regulado=isinstance(producto, ProductoRegulado),
        )
