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