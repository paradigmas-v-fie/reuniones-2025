from .domain import Producto, IVA
from .schemas import ProductCreateSchema, ProductDetailSchema, ProductUpdateSchema
from .repository import Repository
from typing import List


class Service:
    def __init__(self, product_repository: Repository):
        self.product_repository = product_repository

    def add_product(self, product: ProductCreateSchema):
        nuevo_producto = Producto(
            nombre=product.nombre,
            precio_base=product.precio_base,
            iva=IVA(),
        )
        self.product_repository.add_product(nuevo_producto)
        return ProductDetailSchema.from_domain(nuevo_producto)

    def list_products(self) -> List[ProductDetailSchema]:
        return [
            ProductDetailSchema.from_domain(p)
            for p in self.product_repository.list_products()
        ]

    def get_product(self, product_id: str) -> ProductDetailSchema | None:
        producto = self.product_repository.get_product_by_id(product_id)
        if producto:
            return ProductDetailSchema.from_domain(producto)
        return None

    def remove_product(self, product_id: str) -> bool:
        return self.product_repository.remove_product(product_id)

    def update_product(
        self, product_id: str, product_data: ProductUpdateSchema
    ) -> ProductDetailSchema | None:
        producto = self.product_repository.get_product_by_id(product_id)
        if not producto:
            return None

        producto.nombre = product_data.nombre
        producto.precio_base = product_data.precio_base
        if hasattr(producto, "edad_minima") and product_data.edad_minima is not None:
            producto.edad_minima = product_data.edad_minima

        self.product_repository.update_product(producto)
        return ProductDetailSchema.from_domain(producto)
