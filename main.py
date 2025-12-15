from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Dummy product data
dummy_products = [
    {"id": 1, "name": "Product A"},
    {"id": 2, "name": "Product B"},
    {"id": 3, "name": "Product C"},
    {"id": 4, "name": "Product D"},
]

@app.get("/recommendations")
def get_recommendations(user_id: int = Query(..., description="User ID")) -> List[dict]:
    # Simple logic: recommend all products (replace with real logic)
    return dummy_products
