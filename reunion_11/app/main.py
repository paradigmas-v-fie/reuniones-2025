from fastapi import FastAPI

from app.products.router import Router as ProductRouter
from .internal.database import DatabaseConnection

app = FastAPI()

db = DatabaseConnection()
db.connect()
con = db.get_collection("products")

app.include_router(ProductRouter(con).get_router())


@app.get("/")
async def root():
    return {"message": "Hello World"}
