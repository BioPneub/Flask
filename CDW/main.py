from fastapi import FastAPI
from laptop_price import *
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: str


app = FastAPI()


@app.get("/")
async def root(item: Item):
    return item
