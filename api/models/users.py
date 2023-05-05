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
    
    @staticmethod
    async def create_user(payload, avatar_img_file):
        """
        Create user and return user info
        """
        user = Users.create(**payload)
        user.avatar_img_url = await save_avatar_im_to_static(avatar_img_file, user.username)
        user.save()

        user = model_to_dict(user)
        return user
    
    @staticmethod
    def get_user_by_username(username: str) -> dict:
        """
        Get user by username
        """
        user = Users.get_or_none(Users.username == username)
        user = model_to_dict(user)
        return user

    @staticmethod
    def get_user_by_id(user_id: str) -> dict:
        """
        Get user by id
        """
        user = Users.get_or_none(Users.id == user_id)
        user = model_to_dict(user)
        return user
    