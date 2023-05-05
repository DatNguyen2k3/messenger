from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict
from models.messages import Messages
from pydantic import BaseModel
from models import psql_db


router = APIRouter()
db = psql_db

class Message(BaseModel):
    from_user: str
    to_conversation: str
    content: str
    

@router.post("/api/messages/create_table")
def create_messages_table():
    db.connect()
    db.create_tables([Messages])
    db.close()
    

@router.post("/api/messages")
def create_message(payload_: Message):
    """Create a new message"""
    payload = payload_.dict()
    message = Messages.create(**payload)
    
    message_dict = model_to_dict(message)
    return {
        "input": payload,
        "new_message": message_dict
    }
