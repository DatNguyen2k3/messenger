from fastapi import APIRouter, File, UploadFile, Depends, Form
from playhouse.shortcuts import model_to_dict
from models.users import Users
from schemas.user import User, UserResponse
from utils.users import *
from utils import is_valid_email, is_valid_uuid
from typing import List
from models import psql_db as db


router = APIRouter()


@router.post("/api/users/create_table")
def create_users_table():
    db.create_tables([Users])


@router.get("/api/users")
def get_all_users(search_query: str = "") -> List[UserResponse]:
    """Get all users"""
    try:
        users = Users.get_users(search_query)
    except Exception as e:
        return {"error": str(e)}

    return users


@router.post("/api/users")
async def create_user(
    username: str = Form(...), email: str = Form(...), avatar_img_file: UploadFile = File(...)
) -> UserResponse:
    """
    Register user
    if register success, return user info
    if register fail, return error message
    """
    payload_ = User(username=username, email=email)
    payload = payload_.dict()

    # validate email
    if not is_valid_email(payload["email"]):
        return {"error": "Email is not valid"}

    # validate username
    if not is_valid_username(payload["username"]):
        return {"error": "Username is not valid"}

    # check if username or email already exists
    if Users.is_username_exists(payload["username"]) or Users.is_email_exists(
        payload["email"]
    ):
        return {"error": "Username or email already exists"}

    user = await Users.create_user(payload, avatar_img_file)
    return user


@router.get("/api/login")
def login(username: str) -> UserResponse:
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
def get_user(user_id: str) -> UserResponse:
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
