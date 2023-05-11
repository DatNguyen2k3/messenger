from pydantic import BaseModel, validator, Field
from utils import is_valid_uuid
from models.users import Users
from typing import List, TypedDict
import uuid
from enum import Enum
from .user import UserAPI


class ConversationType(str, Enum):
    '''
    Conversation type enum
    '''
    Normal = 'Normal'
    Group = 'Group'

class Conversation(BaseModel):
    '''
    Conversation model
    '''
    created_by: uuid.UUID = Field(default_factory=uuid.uuid4)
    modified_by: uuid.UUID = Field(default_factory=uuid.uuid4)
    type: ConversationType
    members: List[uuid.UUID]
    
    
    
class ConversationAPI(TypedDict):
    id: str
    created_by: UserAPI
    created_at: str
    modified_by: UserAPI
    modified_at: str
    type: ConversationType
    members: List[UserAPI]
    latest_message: str
    name: str
    avatar_img_url: str    

    
    