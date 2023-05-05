from models.users import Users
from settings import AVATAR_IMGS_DIR, DOMAIN
from playhouse.shortcuts import model_to_dict
import uuid


USERNAME_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def is_valid_username(username):
    """
    Check if username is valid
    """
    for char in username:
        if char not in USERNAME_CHARACTERS:
            return False

    return True


def is_username_exists(username):
    """
    Check if username exists
    """
    if Users.select().where(Users.username == username).exists():
        return True
    return False


def is_email_exists(email):
    """
    Check if email exists
    """
    if Users.select().where(Users.email == email).exists():
        return True
    return False

def is_user_id_exists(user_id: str):
    '''
    Check if user id exists
    '''
    if Users.select().where(Users.id == user_id).exists():
        return True
    return False
