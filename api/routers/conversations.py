from fastapi import APIRouter, Query, HTTPException, status
from models.conversations import Conversations
from schemas.conversation import Conversation, ConversationType, ConversationResponse
from models.users import Users
from models import psql_db as db
from typing import Optional, List
import uuid
from services.conversations import format_conversations

router = APIRouter()
    
    
@router.post("/api/conversations/create_table")
def create_conversations_table():
    '''Create conversations table'''
    db.create_tables([Conversations])
    

@router.post("/api/conversations")
def create_conversation(payload_: Conversation) -> ConversationResponse:
    """Create a new conversation"""

    try:
        conversation = Conversations.create_conversation(payload_)
    except Exception as exception:
        return HTTPException(status_code=400, detail=str(exception))
    
    return conversation


@router.get("/api/conversations")
def get_conversations(
    user_id: Optional[uuid.UUID] = Query(None),
    type: Optional[ConversationType] = None, 
    members: Optional[List[uuid.UUID]] = Query(None)
    ) -> List[ConversationResponse]:
    
    """Get conversations"""
    try:
        conversations = Conversations.get_conversations(user_id, type, members)
    except Exception as exception:
        return HTTPException(status_code=400, detail=str(exception))
    
    return format_conversations(conversations, user_id)


@router.get("/api/conversations/{conversation_id}")
def get_single_conversation(conversation_id: uuid.UUID) -> ConversationResponse:
    """Get single conversation"""
    try:
        conversation = Conversations.get_conversation_by_id(conversation_id)
    except Exception as exception:
        return HTTPException(status_code=400, detail=str(exception))
    
    return conversation


    
    