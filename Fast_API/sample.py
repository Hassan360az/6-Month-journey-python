from fastapi import FastAPI, status

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{id}")
def get_user(id: int):

    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "name": "Ali"
    }