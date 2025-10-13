from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Base de datos mock de items
items = ["ID-001", "ID-002", "ID-003"]

class ItemDTO(BaseModel):
    id: str
    price: float | None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items")
async def list_items() -> list[ItemDTO]:
    # Aplico el DTO a cada elemento de la lista
    return list(map(lambda x: ItemDTO(id=x), items))


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> ItemDTO:
    if item_id in items:
        return ItemDTO(id=item_id)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
