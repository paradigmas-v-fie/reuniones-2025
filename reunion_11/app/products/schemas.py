from pydantic import BaseModel
from .domain import ProductoRegulado, Producto
from datetime import datetime
from abc import ABC, abstractmethod
from app.products.domain import (
    IVA,
    RecargoFijo,
    Pesado,
    Promocion,
    Producto,
    ProductoRegulado,
)

import uuid

## SCHEMAS DE FASTAPI
## FastAPI utiliza Pydantic para validación y serialización


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
    # Observe que agregue un id de producto
    id: str

    @staticmethod
    def from_domain(producto: Producto) -> "ProductDetailSchema":
        return ProductDetailSchema(
            nombre=producto.nombre,
            precio_base=producto.precio_base,
            precio_final=producto.precio_final(None),
            etiquetas=[
                mod.etiqueta_fragment()
                for mod in producto.modificadores
                if mod.etiqueta_fragment()
            ],
            regulado=isinstance(producto, ProductoRegulado),
            # Agregamos el id al schema
            id=str(producto.id),
        )


class ProductUpdateSchema(BaseModel):
    nombre: str
    precio_base: float
    edad_minima: int | None = None


###################################################3
## SCHEMAS DE MONGO (SERIALIZACIÓN / DESERIALIZACIÓN)
###################################################3


class ModificadorDbSchema(ABC):

    @abstractmethod
    def to_mongo(self) -> dict[str, any]:
        pass

    @staticmethod
    @abstractmethod
    def from_mongo(data: dict[str, any]):
        pass


class IVADbSchema(ModificadorDbSchema):
    def __init__(self, iva):
        self.iva = iva

    def to_mongo(self) -> dict[str, any]:
        return {
            "tipo": "IVA",
            "porcentaje": 0.21,  # IVA.PORCENTAJE
            "taxfree": self.iva.taxfree,
        }

    @staticmethod
    def from_mongo(data: dict[str, any]):
        iva = IVA()
        iva.taxfree = data.get("taxfree", False)
        return iva


class RecargoFijoDbSchema(ModificadorDbSchema):
    def __init__(self, recargo_fijo):
        self.recargo_fijo = recargo_fijo

    def to_mongo(self) -> dict[str, any]:
        return {"tipo": "RecargoFijo", "recargo": self.recargo_fijo.recargo}

    @staticmethod
    def from_mongo(data: dict[str, any]):

        return RecargoFijo(data["recargo"])


class PesadoDbSchema(ModificadorDbSchema):
    def __init__(self, pesado):
        self.pesado = pesado

    def to_mongo(self) -> dict[str, any]:
        return {
            "tipo": "Pesado",
            "recargo_peso": 3000.0,  # Could be self.pesado.recargo_peso if it's an attribute
        }

    @staticmethod
    def from_mongo(data: dict[str, any]):

        return Pesado()


class PromocionDbSchema(ModificadorDbSchema):
    def __init__(self, promocion):
        self.promocion = promocion

    def to_mongo(self) -> dict[str, any]:
        return {"tipo": "Promocion", "descuento": self.promocion.descuento}

    @staticmethod
    def from_mongo(data: dict[str, any]):

        return Promocion(data["descuento"])


class ModificadorSchemaFactory:
    _schemas = {
        "RecargoFijo": RecargoFijoDbSchema,
        "IVA": IVADbSchema,
        "Pesado": PesadoDbSchema,
        "Promocion": PromocionDbSchema,
    }

    @classmethod
    def get_schema(cls, modificador) -> ModificadorDbSchema:
        modifier_type = modificador.__class__.__name__
        schema_class = cls._schemas.get(modifier_type)

        if not schema_class:
            raise ValueError(f"El modificador no tiene schema: {modifier_type}")

        return schema_class(modificador)

    @classmethod
    def from_mongo(cls, data: dict[str, any]):
        tipo = data.get("tipo")
        schema_class = cls._schemas.get(tipo)

        if not schema_class:
            raise ValueError(f"El modificador no tiene schema: {tipo}")

        return schema_class.from_mongo(data)


class ProductoDbSchema:
    # Sirve tanto para crear como para leer
    @staticmethod
    def from_domain_to_mongo(producto) -> dict[str, any]:
        """Convert domain Producto to MongoDB document"""
        document = {
            "producto_id": str(producto.id),  # Convert UUID to string
            "nombre": producto.nombre,
            "precio_base": producto.precio_base,
            "tipo": "regulado" if hasattr(producto, "edad_minima") else "base",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "active": True,  # For soft deletes
        }

        # Add specific fields for regulated products
        if hasattr(producto, "edad_minima"):
            document["edad_minima"] = producto.edad_minima

        # Serialize modificadores using their specific schemas
        modificadores = []
        for mod in producto.modificadores:
            schema = ModificadorSchemaFactory.get_schema(mod)
            modificadores.append(schema.to_mongo())

        document["modificadores"] = modificadores

        return document

    @staticmethod
    def from_mongo_to_domain(mongo_doc: dict[str, any]):
        # Restaurar modificadores
        modificadores = []
        iva = None

        for mod_doc in mongo_doc.get("modificadores", []):
            if mod_doc.get("tipo") == "IVA":
                iva = ModificadorSchemaFactory.from_mongo(mod_doc)
            else:
                modificador = ModificadorSchemaFactory.from_mongo(mod_doc)
                modificadores.append(modificador)

        if iva is None:
            iva = IVA()

        if mongo_doc.get("tipo") == "regulado":
            producto = ProductoRegulado(
                nombre=mongo_doc["nombre"],
                precio_base=mongo_doc["precio_base"],
                edad_minima=mongo_doc.get("edad_minima", 18),
                iva=iva,
                modificadores=modificadores,
            )
        else:
            producto = Producto(
                nombre=mongo_doc["nombre"],
                precio_base=mongo_doc["precio_base"],
                iva=iva,
                modificadores=modificadores,
            )

        # Restaurar el ID del producto desde el documento
        if "producto_id" in mongo_doc:
            producto.id = uuid.UUID(mongo_doc["producto_id"])

        return producto


class ProductoUpdateDbSchema:
    def __init__(self, producto):
        self.producto = producto

    def to_mongo(self) -> dict[str, any]:
        return {
            "nombre": self.producto.nombre,
            "precio_base": self.producto.precio_base,
            "edad_minima": self.producto.edad_minima,
            "modificadores": [mod.to_mongo() for mod in self.producto.modificadores],
        }

    @staticmethod
    def from_mongo(data: dict[str, any]):

        return ProductoUpdateDbSchema(
            nombre=data["nombre"],
            precio_base=data["precio_base"],
            edad_minima=data.get("edad_minima", 18),
            modificadores=[
                ModificadorSchemaFactory.from_mongo(mod)
                for mod in data.get("modificadores", [])
            ],
        )
