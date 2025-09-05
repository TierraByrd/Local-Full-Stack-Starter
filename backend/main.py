from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

items = []
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# add items
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

# see all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    return items

# see single item
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    return items[item_id]

# update item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

# delete item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    items.pop(item_id)
    return {"message": "Item deleted"}


@app.get("/")
async def root():
    return {"message": "Welcome to the Item API"}

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}