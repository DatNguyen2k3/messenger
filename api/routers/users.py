from fastapi import APIRouter, File, UploadFile, Depends
from playhouse.shortcuts import model_to_dict
from models.users import Users
from schemas.user import User, UserAPI
from utils.users import *
from utils import is_valid_email, is_valid_uuid


router = APIRouter()


# @router.post("/api/users/create_table")
# def create_users_table():
#     db.connect()
#     db.create_tables([Users])
#     db.close()


@router.get("/api/users")
def get_all_users():
    """Get all users"""
    users = Users.select()
    users = [model_to_dict(user) for user in users]
    return users


# @router.post('/api/test_upload_file')
# async def create_upload_file(file: UploadFile = File(...)):
#     img_url = await saveAvatarImgToStatic(file, "test")

#     return {
#         'url': img_url
#     }


# @router.post("/api/users")
# async def create_user(payload_: User = Depends(), avatar_img_file: UploadFile = File(...)):
#     """Create a new user"""
#     print("----------------")
#     payload = payload_.dict()
#     user = Users.create(**payload)
#     user.avatar_img_url = await saveAvatarImgToStatic(avatar_img_file, user.username)
#     user.save()

#     user = model_to_dict(user)
#     return user


# @router.patch("/api/users/{id}")
# def edit_user(id: str, payload_: User):
#     """Update user info"""
#     payload = payload_.dict()
#     user = (
#         Users.update(
#             username=payload["username"],
#             email=payload["email"],
#         )
#         .where(Users.id == id)
#         .execute()
#     )

#     user = model_to_dict(user)
#     return user


# @router.delete("/api/users/{id}")
# def user_employee(id: str):
#     """Delete user"""
#     user = Users.get_by_id(id)
#     user.delete_instance()

#     user = model_to_dict(user)
#     return user


@router.post("/api/register")
async def register(
    payload_: User = Depends(), avatar_img_file: UploadFile = File(...)
) -> UserAPI:
    """
    Register user
    if register success, return user info
    if register fail, return error message
    """
    payload = payload_.dict()

    # validate email
    if not is_valid_email(payload["email"]):
        return {"error": "Email is not valid"}

    # validate username
    if not is_valid_username(payload["username"]):
        return {"error": "Username is not valid"}

    # check if username or email already exists
    if Users.is_username_exists(payload["username"]) or Users.is_email_exists(payload["email"]):
        return {"error": "Username or email already exists"}

    user = await Users.create_user(payload, avatar_img_file)
    return user


@router.get("/api/login")
def login(username: str) -> UserAPI:
    """
    Login user
    If login success, return user info
    If login fail, return error message
    """
    if not is_valid_username(username):
        return {"error": "Username is not valid"}

    user = Users.get_user_by_username(username)
    if not user:
        return {"error": "User does not exist"}
    
    return user

@router.get("/api/users/{user_id}")
def get_user(user_id: str) -> UserAPI:
    """
    Get user by id.
    If user exists, return user info.
    If user does not exist, return error message.
    """
    if not is_valid_uuid(user_id):
        return {"error": "User id is not valid"}
    
    user = Users.get_user_by_id(user_id)
    if not user:
        return {"error": "User does not exist"}
    
    return user
