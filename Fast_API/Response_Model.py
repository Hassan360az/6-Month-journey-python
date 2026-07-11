from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class user(BaseModel):
    name: str
    age: int 
    secret_code: int = 10

class user_data(BaseModel):
    name: str 
    age: int



@app.post("/login", response_model=user)
def user_login (user_input: user):    
    return user_input
