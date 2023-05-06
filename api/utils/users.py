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

