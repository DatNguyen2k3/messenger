from fastapi import APIRouter, File, UploadFile, Depends
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.users import Users
from models.conversations import Conversations, members_validator
from pydantic import BaseModel, Field
import uuid
from models import psql_db
import json
from . import AVATAR_IMGS_DIR, DOMAIN
from utils import saveAvartarImgToStatic, convertFileName


router = APIRouter()
db = psql_db


class Conversation(BaseModel):
    created_by: str
    modified_by: str
    type: str
    members: list
    
    
@router.post("/api/conversations/create_table")
def create_conversations_table():
    db.connect()
    db.create_tables([Conversations])
    db.close()
    

@router.post("/api/conversations")
def create_conversation(payload_: Conversation):
    """Create a new conversation"""
    payload = payload_.dict()
    members_validator(payload['members'])
    conversation = Conversations.create(**payload)
    
    conversation_dict = model_to_dict(conversation)
    return {
        "input": payload,
        "new_conversation": conversation_dict
    }