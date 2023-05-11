from pydantic import BaseModel
import uuid
from typing import TypedDict
from .user import UserAPI
from .conversation import ConversationAPI


class Message(BaseModel):
    from_user: uuid.UUID 
    to_conversation: uuid.UUID
    content: str
    

class MessageAPI(TypedDict):
    id: uuid.UUID
    from_user: UserAPI
    to_conversation: ConversationAPI
    created_at: str
    modified_at: str
    content: str
    is_delete: bool 