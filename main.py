
from fastapi import FastAPI
from tokenise.main import tokenise
from typing import Union


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/tokenise/")
def read_item(phrase: str):
    return {"tokenised phrase:", tokenise(phrase)}
