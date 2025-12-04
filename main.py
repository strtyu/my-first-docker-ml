from fastapi import FastAPI
from pydantic import BaseModel
import torch

app = FastAPI(title="Моя первая моделька в Docker")

class Item(BaseModel):
    x: float

@app.get("/")
def home():
    return {"message": "Привет! Docker работает!", "torch_version": torch.__version__}

@app.post("/predict")
def predict(item: Item):
    result = item.x * 2 + 1
    return {"input": item.x, "prediction": result}