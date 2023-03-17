from fastapi import FastAPI
from grammar_controller import grammar_controller

app = FastAPI()

@app.get("/")
async def root(phrase: str):
    phrase_as_list = phrase.split()
    grammar_controller(phrase_as_list)
