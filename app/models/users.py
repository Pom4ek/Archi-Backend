from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    registered_at: datetime


class User(UserBase):
    id: Optional[int]
    password: str
    registered_at: Optional[datetime]