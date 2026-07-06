from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_items(item_name: str, limit: int = 10):
    return {"query": item_name, "per_page": limit}





