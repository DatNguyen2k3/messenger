from fastapi import APIRouter
from models.messages import Messages
from schemas.message import Message
from models import psql_db
import uuid
from typing import List


router = APIRouter()
db = psql_db
    

@router.post("/api/messages/create_table")
def create_messages_table():
    '''Create messages table'''
    db.create_tables([Messages])
    

@router.post("/api/messages")
def send_message(message: Message) -> dict:
    '''Send message'''
    try:
        message_dict = Messages.create_message(message)
    except Exception as e:
        return {"error": str(e)}
    
    return message_dict

@router.get("/api/messages")
def get_messages(conversation_id: uuid.UUID, limit: int) -> List[dict]:
    '''Get messages'''
    try:
        messages = Messages.get_messages(conversation_id, limit)
    except Exception as e:
        return {"error": str(e)}
    
    return messages


