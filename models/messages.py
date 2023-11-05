import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class Message(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    sender_id: str
    receiver_id: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        schema_extra = {
            "example": {
                "sender_id": "uuid of the sender",
                "receiver_id": "uuid of the receiver",
                "content": "Hey, how's it going?",
                "read": False
            }
        }
        