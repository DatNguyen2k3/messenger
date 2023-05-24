from fastapi import Query
from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from playhouse.postgres_ext import ArrayField
from playhouse.shortcuts import model_to_dict
from utils import format_members
from schemas.conversation import Conversation, ConversationType
from typing import List, Optional

                 
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
    def validate_members(cls, members: List[uuid.UUID]) -> List[uuid.UUID]:
        '''
        Validate conversation members
        '''
        members = format_members(members)
                
        if not isinstance(members, list):
            raise ValueError("Members should be a list")
        
        if len(members) < 2:
            raise ValueError("Members size should be more than 2")
        for member_id in members:
            if not Users.is_user_id_exists(member_id):
                raise ValueError(f"Member {member_id} does not exist")
        return members
    
    @classmethod
    def create_conversation(cls, payload_: Conversation) -> dict:
        '''
        Create a new conversation
        '''
        payload = payload_.dict()
        if payload['type'] == 'Normal':
            payload['members'] = cls.validate_members(payload['members'])
            
        if cls.select().where(cls.members == payload['members']).exists():
            raise ValueError('Conversation already exists') 
        
        conversation = cls.create(**payload)
        conversation_dict = model_to_dict(conversation)
        return conversation_dict


    @classmethod
    def get_conversation_by_id(cls, conversation_id: uuid.UUID) -> dict:
        '''
        Get conversation by id
        '''
        conversation = cls.get_or_none(cls.id == conversation_id)
        if conversation is None:
            raise Exception('Conversation not found')
        
        conversation_dict = model_to_dict(conversation)
        return conversation_dict
        
    
    @classmethod
    def get_conversations(
        cls, 
        user_id: Optional[uuid.UUID] = Query(None),
        type: Optional[ConversationType] = None, 
        members: Optional[List[uuid.UUID]] = Query(None)
        ) -> List[dict]:
        '''
        Get normal conversation by members
        '''
        
        where_clause = p.Expression(lhs=1, op='=', rhs=1)
        if type is not None:
            where_clause &= (cls.type == type)
        
        if members is not None:
            members = cls.validate_members(members)
            where_clause &= (cls.members == members) 
            
        if user_id is not None:
            where_clause &= (cls.members.contains([user_id])) 
        
        conversations = cls.select().where(where_clause).order_by(cls.modified_at.desc())
        conversations_list = [model_to_dict(conversation)
                              for conversation in conversations]
        return conversations_list