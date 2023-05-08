from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from playhouse.shortcuts import model_to_dict
from services.users import save_avatar_im_to_static


class Users(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    username = p.CharField(max_length=255, unique=True)
    email = p.CharField(max_length=255, unique=True)
    avatar_img_url = p.CharField(max_length=1000, null=True)
    created_at = p.DateTimeField(default= datetime.datetime.now)
    modified_at = p.DateTimeField(default= datetime.datetime.now)
    
    @classmethod
    async def create_user(cls, payload: dict, avatar_img_file: bytes) -> dict:
        """
        Create user and return user info
        """
        user = Users.create(**payload)
        user.avatar_img_url = await save_avatar_im_to_static(avatar_img_file, user.username)
        user.save()

        user = model_to_dict(user)
        return user
    
    @classmethod
    def get_user_by_username(cls, username: str) -> dict:
        """
        Get user by username
        """
        
        user = Users.get_or_none(Users.username == username)
        if user is None:
            return None
        
        user = model_to_dict(user)
        return user

    @classmethod
    def get_user_by_id(cls, user_id: str) -> dict:
        """
        Get user by id
        """
        
        user = Users.get_or_none(Users.id == user_id)
        if user is None:
            return None
        
        user = model_to_dict(user)
        return user
    
    
    @classmethod
    def is_username_exists(cls, username: str) -> bool:
        """
        Check if username exists
        """
        if Users.select().where(Users.username == username).exists():
            return True
        return False


    @classmethod
    def is_email_exists(cls, email: str) -> bool:
        """
        Check if email exists
        """
        if Users.select().where(Users.email == email).exists():
            return True
        return False


    @classmethod
    def is_user_id_exists(cls, user_id: str) -> bool:
        '''
        Check if user id exists
        '''
        if Users.select().where(Users.id == user_id).exists():
            return True
        return False

    