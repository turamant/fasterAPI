from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Adidas",
    },
    2: {
        "name": "Whater",
        "price": 1.23,
        "brand": "Reebook",
    },
}

@app.get("/")
def home():
    return {"DATA": "TEST"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description='The id of the item you`d like to view', gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(item_id: int, test: int, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"DATA": "Not found"}

@app.get("/get-by-name")
def get_item(name: str = Query(None, title="Name", description="name of item")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"DATA": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "item ID already exists."}

    inventory[item_id] = {"name": item.name, "price": item.price,
                          "brand": item.brand}
    return inventory[item_id]


@app.get("/about")
def about():
    return {"DATA": "ABOUT"}
