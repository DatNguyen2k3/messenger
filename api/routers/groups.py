from fastapi import APIRouter, File, UploadFile, Depends
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.users import Users
from models.messages import Messages
from models.groups import Groups
from models.conversations import Conversations, members_validator
from pydantic import BaseModel, Field
import uuid
from models import psql_db
import json
from . import AVATAR_IMGS_DIR, DOMAIN
from utils import saveAvartarImgToStatic, convertFileName


router = APIRouter()
db = psql_db

class Group(BaseModel):
    name: str
    conversation: str
    

@router.post("/api/groups/create_table")
def create_groups_table():
    db.connect()
    db.create_tables([Groups])
    db.close()
    

@router.post("/api/groups")
def create_group(payload_: Group):
    """Create a new group"""
    payload = payload_.dict()
    group = Groups.create(**payload)
    
    group_dict = model_to_dict(group)
    return {
        "input": payload,
        "new_group": group_dict
    }