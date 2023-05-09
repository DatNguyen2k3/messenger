from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from .conversations import Conversations
from schemas.message import Message   
from playhouse.shortcuts import model_to_dict
            
class Messages(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    from_user = p.ForeignKeyField(Users, backref='from_user')
    to_conversation = p.ForeignKeyField(Conversations, backref='to_conversation')    
    created_at = p.DateTimeField(default=datetime.datetime.now)
    modified_at = p.DateTimeField(default=datetime.datetime.now)
    is_deleted = p.BooleanField(default=False)
    content = p.TextField()
    
    
    @classmethod
    def create_message(cls, payload_: Message) -> dict:
        '''Create message'''
        payload = payload_.dict()
        
        to_conversation = Conversations.get_by_id(payload['to_conversation'])
        if payload['from_user'] not in to_conversation.members:
            raise ValueError("User is not a member of the conversation")
        
        message = cls.create(**payload)
        message_dict = model_to_dict(message)
        return message_dict