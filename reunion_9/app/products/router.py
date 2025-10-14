from fastapi import APIRouter
from .service import Service
from .schemas import ProductCreateSchema, ProductDetailSchema

class Router:
    def __init__(self):
        self._router = APIRouter(
            prefix="/productos",
            tags=["productos"],
            responses={404: {"description": "Not found"}},
        )
        self._service = Service()
        self._router.add_api_route("/", self.list_products, methods=["GET"])
        self._router.add_api_route("/", self.create_product, methods=["POST"])

    def list_products(self) -> list[ProductDetailSchema]:
        print("Listing products")
        return self._service.list_products()

    # Es necesario aclarar el schema de entrada para que FastAPI pueda relacionar el body
    def create_product(self, product: ProductCreateSchema) -> ProductDetailSchema:
        print("Creating product:", product)
        return self._service.add_product(product)

    def get_router(self):
        return self._router
