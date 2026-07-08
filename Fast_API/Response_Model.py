from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class user(BaseModel):
    name = str
    age = int 
    secret_code = 10

class user_data(BaseModel):
    name = str
    age = int



@app.post("/login", response_model=user)
def user_login (user: user):
    return user_data
