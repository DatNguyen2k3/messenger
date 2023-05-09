from fastapi import APIRouter, Query
from playhouse.shortcuts import model_to_dict
from models.conversations import Conversations
from schemas.conversation import Conversation, ConversationType
from models.users import Users
from models import psql_db
from typing import Optional, List
import uuid


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
    except Exception as exception:
        return {'error': str(exception)}
    
    return conversation


@router.get("/api/conversations")
def get_conversations(
    type: Optional[ConversationType] = None, 
    members: Optional[List[uuid.UUID]] = Query(None)
    ) -> List[dict]:
    
    """Get conversations"""
    try:
        conversations = Conversations.get_conversations(type, members)
    except Exception as exception:
        return {'error': str(exception)}
    
    return conversations


@router.get("/api/conversations/{conversation_id}")
def get_single_conversation(conversation_id: uuid.UUID) -> dict:
    """Get single conversation"""
    try:
        conversation = Conversations.get_conversation_by_id(conversation_id)
    except Exception as exception:
        return {'error': str(exception)}
    
    return conversation


    
    