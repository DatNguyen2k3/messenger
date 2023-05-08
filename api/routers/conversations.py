from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict
from models.conversations import Conversations
from schemas.conversation import Conversation
from models.users import Users
from utils.conversations import validate_members
from models import psql_db


router = APIRouter()
db = psql_db
    
    
@router.post("/api/conversations/create_table")
def create_conversations_table():
    '''Create conversations table'''
    db.create_tables([Conversations])
    

@router.post("/api/conversations")
def create_conversation(payload_: Conversation):
    """Create a new conversation"""
    payload = payload_.dict()
    
    # Check if conversation type is valid
    if not Conversations.is_valid_conversation_type(payload['type']):
        return {'error': 'Invalid conversation type'}
    
    # Check if members are valid
    try :
        payload['members'] = validate_members(payload['members'])
    except ValueError as value_error:
        return {'error': str(value_error)}
    
    # Create conversation
    conversation = Conversations.create(**payload)
    conversation_dict = model_to_dict(conversation)
    
    return conversation_dict
