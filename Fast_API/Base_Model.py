from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class password(BaseModel):
    password: int


@app.post("/password")
def password_post(password: password):
    return{"password" , password.password}