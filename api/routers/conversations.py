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
    
    conversation = Conversations.create_conversation(payload)
    return conversation


@router.get("/api/conversations")
def get_conversations() -> list:
    """Get all conversations"""
    conversations = Conversations.select()
    conversations_list = [model_to_dict(conversation) for conversation in conversations]
    return conversations_list


@router.get("/api/conversations/{conversation_id}")
def get_single_conversation(conversation_id: str) -> dict:
    """Get single conversation"""
    try:
        conversation = Conversations.get_conversation_by_id(conversation_id)
    except ValueError as value_error:
        return {'error': str(value_error)}
    
    return conversation

    
    