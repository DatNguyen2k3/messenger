from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict
from models.conversations import Conversations
from schemas.conversation import Conversation
from models.users import Users
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
    
    try: 
        conversation = Conversations.create_conversation(payload_)
    except ValueError as value_error:
        return {'error': str(value_error)}
    
    return conversation


@router.get("/api/conversations")
def get_conversations() -> list:
    """Get all conversations"""
    conversations = Conversations.select()
    conversations_list = [model_to_dict(conversation) for conversation in conversations]
    return conversations_list


@router.get("/api/conversations/normal/member1={member1}&member2={member2}")
def get_normal_conversation(member1: str, member2: str) -> dict:
    """Get normal conversation by members"""
    
    try :
        conversation = Conversations.get_normal_conversation_by_members([member1, member2])
    except ValueError as value_error:
        return {'error': str(value_error)}
    
    return conversation


@router.get("/api/conversations/{conversation_id}")
def get_single_conversation(conversation_id: str) -> dict:
    """Get single conversation"""
    try:
        conversation = Conversations.get_conversation_by_id(conversation_id)
    except ValueError as value_error:
        return {'error': str(value_error)}
    
    return conversation


    
    