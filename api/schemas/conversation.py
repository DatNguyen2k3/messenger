from pydantic import BaseModel, validator, Field
from utils import is_valid_uuid
from models.users import Users
from typing import List
import uuid
from enum import Enum


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
    
    