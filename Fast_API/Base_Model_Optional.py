from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class profile (BaseModel):
    username: str
    Father_Name: Optional[str] = None