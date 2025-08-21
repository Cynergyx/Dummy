
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from response import response1, response2, response3, response4, response5, response6, response7
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


# Accepts optional 'response_id' query parameter to select a specific response (1-7)
@app.post("/chat")
async def read_root(prompt: DummyData, response_id: int = None):
    responses = [response1, response2, response3, response4, response5, response6, response7]
    if response_id is not None:
        # Clamp response_id to valid range
        idx = max(1, min(response_id, len(responses)))
        return responses[idx - 1]
    else:
        return random.choice(responses)

# For deployment: allow running with `python app.py` or via ASGI server


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

