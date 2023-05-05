from models.users import Users
from routers import AVATAR_IMGS_DIR, DOMAIN
from playhouse.shortcuts import model_to_dict


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
