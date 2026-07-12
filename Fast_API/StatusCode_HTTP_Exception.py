from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# @app.post ("/users", status_code=status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "Message": "user Created"
#     }

@app.get("/pages/{id}")
def get_page (id: int):
    if id !=1:
        raise HTTPException(
            status_code=404,
            detail="user is not in this"
        )

    return {
        "name": "Random"
    }