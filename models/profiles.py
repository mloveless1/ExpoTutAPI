from typing import Optional
from pydantic import BaseModel, Field


class Profile(BaseModel):
    # The ID will be provided from the User's ID during creation
    id: Optional[str]
    name: str = Field(...)
    age: int = Field(...)
    bio: str = Field(...)
    orientation: str = Field(...)
    occupation: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    gender: str = Field(...)
    height: str = Field(...)


class ProfileUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    bio: Optional[str]
    orientation: Optional[str]
    occupation: Optional[str]
    city: Optional[str]
    state: Optional[str]
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
                "city": "Long Beach",
                "state": "CA",
                "gender": "Male",
                "height": "5'8"
            }
        }
