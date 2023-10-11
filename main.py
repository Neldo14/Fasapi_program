from fastapi import FastAPI
from typing import Union

# creamos la app

app= FastAPI()
@app.get("/")
def read_root():
    return {"Hi!": "I am Gineldo"};

@app.get("/hi")
def read_root():
    return {"Hi!": "I am Gineldo"};



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q": q}