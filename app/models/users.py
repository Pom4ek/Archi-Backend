from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str
    

class UserRead(UserBase):
    id: int
    registered_at: datetime
    

class User(UserBase):
    id: int
    password: str
    registered_at: datetime