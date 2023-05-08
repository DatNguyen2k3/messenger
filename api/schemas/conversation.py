from pydantic import BaseModel


class Conversation(BaseModel):
    '''
    Conversation model
    '''
    created_by: str
    modified_by: str
    type: str
    members: list