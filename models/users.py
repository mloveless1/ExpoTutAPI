import uuid

from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str
    password: str  # In real-world applications, never store plain-text passwords. Use hashing.


class UserIn(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]  # Remember to hash the password before storing
