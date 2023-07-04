from fastapi import FastAPI
from grammar_controller import grammar_controller
import time
app = FastAPI()

@app.get("/")
async def root(phrase: str):
    start = time.time()
    word_object_list = grammar_controller(phrase)
    end = time.time()
    return {
        "time": end - start,
        "word_object_list": word_object_list
    }
