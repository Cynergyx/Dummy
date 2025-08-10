
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from response import response1, response2
from fastapi.middleware.cors import CORSMiddleware
import random
import os
from uvicorn import run


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# For deployment: allow running with `python app.py` or via ASGI server
if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 8000))  # Retrieve PORT or default to 4000
    except ValueError:  # Handle invalid PORT values
        print("Invalid PORT environment variable. Using default port 4000.")
        port = 4000
    run(app, host="0.0.0.0", port=port)

