from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from response import response1, response2
import random

app = FastAPI()

class DummyData(BaseModel):
    prompt: str



@app.post("/chat")
async def read_root(prompt: DummyData):
    # random function for selecting response
    random_number = random.randint(1, 2)
    if random_number == 1:
        return response1
    else:
        return response2

