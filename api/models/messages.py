from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from .conversations import Conversations
from schemas.message import Message   
            
class Messages(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    from_user = p.ForeignKeyField(Users, backref='from_user')
    to_conversation = p.ForeignKeyField(Conversations, backref='to_conversation')    
    created_at = p.DateTimeField(default=datetime.datetime.now)
    modified_at = p.DateTimeField(default=datetime.datetime.now)
    is_deleted = p.BooleanField(default=False)
    content = p.TextField()