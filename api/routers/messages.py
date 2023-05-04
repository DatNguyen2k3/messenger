from fastapi import APIRouter, File, UploadFile, Depends
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.users import Users
from models.messages import Messages
from models.conversations import Conversations, members_validator
from pydantic import BaseModel, Field
import uuid
from models import psql_db
import json
from . import AVATAR_IMGS_DIR, DOMAIN
from utils import saveAvartarImgToStatic, convertFileName


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
