from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Base de datos mock de items
items = [
    {"id": "ID-002", "price": 10},
    {"id": "ID-003", "price": 20},
    {"id": "ID-004", "price": 30},
]


class ItemDTO(BaseModel):
    id: str
    price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def list_items() -> list[ItemDTO]:
    # Aplico el DTO a cada elemento de la lista
    return list(map(lambda x: ItemDTO(**x), items))


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> ItemDTO:
    for item in items:
        if item.get("id") == item_id:
            return ItemDTO(**item)
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(item_id: str) -> ItemDTO:
    for item in items:
        if item.get("id") == item_id:
            response = ItemDTO(**item)
            items.remove(item)
            return response
    raise HTTPException(status_code=404, detail="Item not found")
