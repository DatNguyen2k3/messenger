from models.users import Users
from . import is_valid_uuid


def validate_members(members: list) -> bool:
    '''
    Check if members are valid
    '''
    members = sorted(list(set(members)))
    
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
