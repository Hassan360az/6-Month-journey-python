from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Confirmed(BaseModel):
    name: str
    age: int


@app.post("/user-confirm")
def user_confirmed(user: Confirmed):
    return {
        "Name": user.name, "Age": user.age
    }