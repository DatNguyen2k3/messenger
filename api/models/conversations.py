from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from playhouse.postgres_ext import ArrayField
from services.conversations import summary_conversation
from playhouse.shortcuts import model_to_dict
from utils import is_valid_uuid
from schemas.conversation import Conversation

                 
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
    def create_conversation(cls, payload_: Conversation) -> dict:
        '''
        Create a new conversation
        '''
        payload = payload_.dict()
        try:
            conversation = Conversations.create(**payload)
        except Exception as exception:
            raise ValueError(str(exception))
        
        conversation_dict = model_to_dict(conversation)
        conversation_dict = summary_conversation(conversation_dict)
        return conversation_dict


    @classmethod
    def get_conversation_by_id(cls, conversation_id: str) -> dict:
        '''
        Get conversation by id
        '''
        if not is_valid_uuid(conversation_id):
            raise ValueError('Invalid uuid')
        
        conversation = Conversations.get_or_none(Conversations.id == conversation_id)
        if conversation is None:
            raise ValueError('Conversation not found')
        
        conversation_dict = model_to_dict(conversation)
        conversation_dict = summary_conversation(conversation_dict)
        return conversation_dict
        
    
    @classmethod
    def get_normal_conversation_by_members(cls, members: list) -> dict:
        '''
        Get normal conversation by members
        '''
        
        # Check if members are valid
        try:
            members = Conversation.validate_members(members)
        except ValueError as value_error:
            raise ValueError(str(value_error))
        
        # Get conversation
        conversation = Conversations.get_or_none(Conversations.members == members)
        if not conversation:
            raise ValueError('Conversation not found')
        
        conversation_dict = model_to_dict(conversation)
        conversation_dict = summary_conversation(conversation_dict)
        return conversation_dict


    def get_conversation_name_for_member(self, member: str) -> str:
        '''
        Get conversation name
        '''
        if self.type == 'Normal':
            other_member_id = self.members[0] if self.members[0] != member else self.members[1]
            other_member = Users.get_user_by_id(other_member_id)
            if other_member is None:
                return 'Unknown'

            return other_member['username']
        
        