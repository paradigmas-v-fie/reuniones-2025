from .domain import Producto, IVA
from .schemas import ProductCreateSchema, ProductDetailSchema
from typing import List

class Service:
    def __init__(self):
        self._products: List[Producto] = []  # type: List[Producto]

    def add_product(self, product: ProductCreateSchema):
        nuevo_producto = Producto(
            nombre=product.nombre,
            precio_base=product.precio_base,
            iva=IVA(),
        )
        # Persisto en mi "base de datos" mock
        self._products.append(nuevo_producto)
        return ProductDetailSchema.from_domain(nuevo_producto)

    def list_products(self) -> List[ProductDetailSchema]:
        return [ProductDetailSchema.from_domain(p) for p in self._products]
