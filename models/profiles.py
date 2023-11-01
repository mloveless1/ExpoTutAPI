import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Profile(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    age: int = Field(...)
    bio: str = Field(...)
    orientation: str = Field(...)
    occupation: str = Field(...)
    location: str = Field(...)
    gender: str = Field(...)
    height: str = Field(...)


class BookUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    bio: Optional[str]
    orientation: Optional[str]
    occupation: Optional[str]
    location: Optional[str]
    gender: Optional[str]
    height: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Don Quixote",
                "age": 30,
                "bio": "Don Quixote is a Spanish novel by Miguel de Cervantes...",
                "orientation": "Straight",
                "occupation": "Programmer",
                "location": "Long Beach",
                "gender": "Male",
                "height": "5'8"
            }
        }
