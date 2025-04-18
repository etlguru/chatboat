from fastapi import FastAPI
from app.model import generate_text

app = FastAPI()

@app.get("/generate")
def generate(prompt: str):
    return {"response": generate_text(prompt)}
