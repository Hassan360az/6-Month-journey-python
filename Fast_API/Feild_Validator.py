from fastapi import FastAPI
from pydantic import BaseModel , field_validator

app = FastAPI()

class UserName(BaseModel):
    name: str

@field_validator("name")
@classmethod
def check_name(cls, value: str) -> str:
    if value == "ali":
        raise value ("Name Shoud not be ali")
    return value.upper()
