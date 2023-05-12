from pydantic import BaseModel
import uuid
from typing import TypedDict
from .user import UserResponse
from .conversation import ConversationResponse


class Message(BaseModel):
    from_user: uuid.UUID 
    to_conversation: uuid.UUID
    content: str
    

class MessageResponse(TypedDict):
    id: uuid.UUID
    from_user: UserResponse
    to_conversation: ConversationResponse
    created_at: str
    modified_at: str
    content: str
    is_delete: bool 