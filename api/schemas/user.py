from pydantic import BaseModel
from typing import TypedDict


class User(BaseModel):
    """
    User model
    """

    email: str
    username: str


class UserResponse(TypedDict):
    '''
    User API
    '''
    id: str
    email: str
    username: str
    avatar_img_url: str
    created_at: str
    modified_at: str