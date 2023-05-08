from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from playhouse.postgres_ext import ArrayField
from utils.conversations import validate_members
from playhouse.shortcuts import model_to_dict

               
         
class Conversations(PeeWeeBaseModel):
    '''
    Conversations model
    '''
    CONVERSATION_TYPES = [
        ('Normal', 'Normal'),
        ('Group', 'Group')
    ]
            
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    created_by = p.ForeignKeyField(Users, backref='created_user')
    created_at = p.DateTimeField(default=datetime.datetime.now)
    modified_by = p.ForeignKeyField(Users, backref='modified_user')    
    modified_at = p.DateTimeField(default=datetime.datetime.now)
    type = p.CharField(choices=CONVERSATION_TYPES, default='Normal')
    members = ArrayField(p.TextField, default=[])