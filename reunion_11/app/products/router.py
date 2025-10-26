from fastapi import APIRouter, HTTPException, status, Response
from .service import Service
from .schemas import ProductCreateSchema, ProductDetailSchema, ProductUpdateSchema
from .repository import Repository


class Router:
    def __init__(self, db):
        self._router = APIRouter(
            prefix="/productos",
            tags=["productos"],
            responses={
                404: {"description": "Product not found"},
                400: {"description": "Bad request"},
                500: {"description": "Internal server error"},
            },
        )
        self._repository = Repository(db=db)
        self._service = Service(self._repository)
        self._router.add_api_route(
            "/",
            self.list_products,
            methods=["GET"],
            response_model=list[ProductDetailSchema],
            status_code=status.HTTP_200_OK,
            summary="List all products",
            responses={
                200: {"description": "Products retrieved successfully"},
                204: {"description": "No products found"},
            },
        )

        self._router.add_api_route(
            "/",
            self.create_product,
            methods=["POST"],
            response_model=ProductDetailSchema,
            status_code=status.HTTP_201_CREATED,
            summary="Create a new product",
            responses={
                201: {"description": "Product created successfully"},
                400: {"description": "Invalid product data"},
            },
        )

        self._router.add_api_route(
            "/{product_id}",
            self.get_product,
            methods=["GET"],
            response_model=ProductDetailSchema,
            status_code=status.HTTP_200_OK,
            summary="Get product by ID",
            responses={
                200: {"description": "Product found"},
                404: {"description": "Product not found"},
            },
        )

        self._router.add_api_route(
            "/{product_id}",
            self.remove_product,
            methods=["DELETE"],
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a product",
            responses={
                204: {"description": "Product deleted successfully"},
                404: {"description": "Product not found"},
            },
        )

        self._router.add_api_route(
            "/{product_id}",
            self.update_product,
            methods=["PATCH"],
            response_model=ProductDetailSchema,
            status_code=status.HTTP_200_OK,
            summary="Update a product",
            responses={
                200: {"description": "Product updated successfully"},
                404: {"description": "Product not found"},
                400: {"description": "Invalid product data"},
            },
        )

    def list_products(self, response: Response) -> list[ProductDetailSchema]:
        try:
            products = self._service.list_products()
            if not products:
                response.status_code = status.HTTP_204_NO_CONTENT
                return []

            return products
        except Exception as e:
            print(f"Error listing products: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while retrieving products",
            )

    # Es necesario aclarar el schema de entrada para que FastAPI pueda relacionar el body
    def create_product(self, product: ProductCreateSchema) -> ProductDetailSchema:
        try:
            created_product = self._service.add_product(product)

            if not created_product:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create product",
                )

            return created_product

        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            print(f"Error creating product: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while creating the product",
            )

    def get_product(self, product_id: str) -> ProductDetailSchema:
        try:
            product = self._service.get_product(product_id)

            if product is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with id '{product_id}' not found",
                )

            return product

        except HTTPException:
            raise
        except Exception as e:
            print(f"Error getting product {product_id}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while retrieving the product",
            )

    def remove_product(self, product_id: str) -> None:
        try:
            success = self._service.remove_product(product_id)

            if not success:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with id '{product_id}' not found",
                )

            return None

        except HTTPException:
            raise
        except Exception as e:
            print(f"Error removing product {product_id}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while deleting the product",
            )

    def update_product(
        self, product_id: str, product_data: ProductUpdateSchema
    ) -> ProductDetailSchema | None:
        try:
            updated_product = self._service.update_product(product_id, product_data)

            if updated_product is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Product with id '{product_id}' not found",
                )

            return updated_product

        except HTTPException:
            raise
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            print(f"Error updating product {product_id}: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An error occurred while updating the product",
            )

    def get_router(self):
        return self._router
