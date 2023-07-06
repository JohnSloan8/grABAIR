
from fastapi import FastAPI
from tokenise.main import tokenise
from typing import Union
import json
from config import ROOT_DIR
import os

app = FastAPI()


with open(os.path.join(ROOT_DIR, 'wordData',  'wordObjectDictionary.json')) as f:
    all_word_data = json.load(f)

@app.post("/tokenise/")
def read_item(phrase: str):
    return {"tokenised phrase:", tokenise(phrase)}
