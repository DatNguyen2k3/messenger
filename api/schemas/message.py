from pydantic import BaseModel
import uuid


class Message(BaseModel):
    from_user: uuid.UUID 
    to_conversation: uuid.UUID
    content: str