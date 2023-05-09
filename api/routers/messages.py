from fastapi import APIRouter
from models.messages import Messages
from schemas.message import Message
from models import psql_db


router = APIRouter()
db = psql_db
    

@router.post("/api/messages/create_table")
def create_messages_table():
    '''Create messages table'''
    db.create_tables([Messages])