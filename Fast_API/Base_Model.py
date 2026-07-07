from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel , Field

app = FastAPI()

class Person(BaseModel):
    name: str = Field (..., min_length=4)
    age: int = Field (..., gt=1)

@app.post("/create_user")
def user_create(person: Person):
    return {
        "message": "Checked"
            
    }

