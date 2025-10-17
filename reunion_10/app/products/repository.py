from .domain import Producto, IVA, RecargoFijo, Promocion
from .schemas import ProductoDbSchema
from pymongo.collection import Collection


class Repository:
    def __init__(self, db):
        self.collection: Collection = db["products"]

    def add_product(self, product: Producto):
        product_dict = ProductoDbSchema.from_domain_to_mongo(product)
        self.collection.insert_one(product_dict)

    def get_product_by_id(self, product_id: str) -> Producto | None:
        product_data = self.collection.find_one({"producto_id": product_id})
        if product_data:
            return ProductoDbSchema.from_mongo_to_domain(product_data)
        return None

    def remove_product(self, product_id: str):
        result = self.collection.delete_one({"producto_id": product_id})
        return result.deleted_count > 0

    def list_products(self) -> list[Producto]:
        products = []
        for product_data in self.collection.find():
            products.append(ProductoDbSchema.from_mongo_to_domain(product_data))
        return products

    def update_product(self, product: Producto):
        product_dict = ProductoDbSchema.from_domain_to_mongo(product)
        result = self.collection.update_one(
            {"producto_id": str(product.id)}, {"$set": product_dict}
        )
        return result.modified_count > 0
