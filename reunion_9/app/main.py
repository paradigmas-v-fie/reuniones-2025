from fastapi import FastAPI

from app.products.router import Router as ProductRouter

app = FastAPI()

app.include_router(ProductRouter().get_router())


@app.get("/")
async def root():
    return {"message": "Hello World"}
