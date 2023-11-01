from typing import Optional
from pydantic import BaseModel, Field


class Profile(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    age: int = Field(...)
    bio: str = Field(...)
    orientation: str = Field(...)
    occupation: str = Field(...)
    location: str = Field(...)
    gender: str = Field(...)
    height: str = Field(...)

    class Config:
        orm_mode = True


class ProfileUpdate(BaseModel):
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
                "name": "John Doe",
                "age": 30,
                "bio": "John Doe is an anonymous individual...",
                "orientation": "Straight",
                "occupation": "Software Developer",
                "location": "New York",
                "gender": "Male",
                "height": "5'9"
            }
        }


