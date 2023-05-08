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
    
    @classmethod
    def is_valid_conversation_type(cls, conversation_type):
        '''
        Check if conversation type is valid
        '''
        return conversation_type in [type[0] for type in cls.CONVERSATION_TYPES]
    
    
    @classmethod
    def create_conversation(cls, payload: dict) -> dict:
        '''
        Create a new conversation
        '''
        # Check if conversation type is valid
        if not Conversations.is_valid_conversation_type(payload['type']):
            return {'error': 'Invalid conversation type'}
        
        # Check if members are valid
        try :
            payload['members'] = validate_members(payload['members'])
        except ValueError as value_error:
            return {'error': str(value_error)}
        
        # Create conversation
        conversation = Conversations.create(**payload)
        conversation_dict = model_to_dict(conversation)
        
        return conversation_dict

