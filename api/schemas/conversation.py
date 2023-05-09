from pydantic import BaseModel, validator
from utils import is_valid_uuid
from models.users import Users

class Conversation(BaseModel):
    '''
    Conversation model
    '''
    created_by: str
    modified_by: str
    type: str
    members: list
    
    
    @classmethod
    def convert_members_to_sorted_list(cls, members):
        '''
        Convert members to sorted list
        '''
        return sorted(list(set(members)))
    
    @validator('type')
    def validate_type(cls, value):
        '''
        Validate conversation type
        '''
        
        if value not in ['Normal', 'Group']:
            raise ValueError('Invalid conversation type')
        return value
    
    
    @validator('members')
    def validate_members(cls, members):
        '''
        Validate conversation members
        '''
        members = Conversation.convert_members_to_sorted_list(members)
                
        if not isinstance(members, list):
            raise ValueError("Members should be a list")
        
        if len(members) < 2:
            raise ValueError("Members size should be more than 2")
        for member_id in members:
            if not is_valid_uuid(member_id):
                raise ValueError(f"Invalid member id: {member_id}")
            if not Users.is_user_id_exists(member_id):
                raise ValueError(f"Member {member_id} does not exist")
        return members
    
    