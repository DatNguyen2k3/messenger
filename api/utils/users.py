from models.users import Users
from routers import AVATAR_IMGS_DIR, DOMAIN
from playhouse.shortcuts import model_to_dict
import uuid


USERNAME_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"


def convertFileName(file, newFileName):
    """
    Convert file name to new file name
    """
    oldFileName = file.filename
    tail_index = oldFileName.rfind(".")
    return newFileName + oldFileName[tail_index:]


async def saveAvartarImgToStatic(file, fileName):
    """
    Save avatar image to static folder
    """
    file.filename = convertFileName(file, fileName)
    contents = await file.read()
    # save the file
    with open(f"{AVATAR_IMGS_DIR}{file.filename}", "wb") as f:
        f.write(contents)
    return DOMAIN + AVATAR_IMGS_DIR + file.filename


def valid_username(username):
    """
    Check if username is valid
    """
    if username == "":
        return False

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

def is_valid_uuid(val):
    '''
    Check if val is valid uuid
    '''
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def is_user_id_exists(user_id: uuid.UUID):
    '''
    Check if user id exists
    '''
    if Users.select().where(Users.id == user_id).exists():
        return True
    return False


async def create_user(payload, avartar_img_file):
    """
    Create user and return user info
    """
    user = Users.create(**payload)
    user.avatar_img_url = await saveAvartarImgToStatic(avartar_img_file, user.username)
    user.save()

    user = model_to_dict(user)
    return user


def get_user_by_username(username: str) -> dict:
    """
    Get user by username
    """
    user = Users.get_or_none(Users.username == username)
    user = model_to_dict(user)
    return user

def get_user_by_id(user_id: uuid.UUID) -> dict:
    """
    Get user by id
    """
    user = Users.get_or_none(Users.id == user_id)
    user = model_to_dict(user)
    return user
