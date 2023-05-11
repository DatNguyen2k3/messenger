from fastapi import APIRouter, Query
from models.conversations import Conversations
from schemas.conversation import Conversation, ConversationType, ConversationAPI
from models.users import Users
from models import psql_db
from typing import Optional, List
import uuid
from services.conversations import format_conversations

router = APIRouter()
db = psql_db
    
    
@router.post("/api/conversations/create_table")
def create_conversations_table():
    '''Create conversations table'''
    db.create_tables([Conversations])
    

@router.post("/api/conversations")
def create_conversation(payload_: Conversation) -> ConversationAPI:
    """Create a new conversation"""

    try:
        conversation = Conversations.create_conversation(payload_)
    except Exception as exception:
        return {'error': str(exception)}
    
    return conversation


@router.get("/api/conversations")
def get_conversations(
    user_id: Optional[uuid.UUID] = Query(None),
    type: Optional[ConversationType] = None, 
    members: Optional[List[uuid.UUID]] = Query(None)
    ) -> List[ConversationAPI]:
    
    """Get conversations"""
    try:
        conversations = Conversations.get_conversations(user_id, type, members)
    except Exception as exception:
        return {'error': str(exception)}
    
    return format_conversations(conversations, user_id)


@router.get("/api/conversations/{conversation_id}")
def get_single_conversation(conversation_id: uuid.UUID) -> ConversationAPI:
    """Get single conversation"""
    try:
        conversation = Conversations.get_conversation_by_id(conversation_id)
    except Exception as exception:
        return {'error': str(exception)}
    
    return conversation


    
    