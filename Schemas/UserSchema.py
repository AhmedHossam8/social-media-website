from typing import Optional
from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str
    password: str
    photo_url: Optional[str]
    