from fastapi import APIRouter, File, UploadFile, Depends
from playhouse.shortcuts import model_to_dict
from peewee import fn
from models.users import Users
from pydantic import BaseModel, Field
import uuid
from models import psql_db
import json
from . import AVATAR_IMGS_DIR, DOMAIN
from utils import saveAvartarImgToStatic, convertFileName
from email_validator import validate_email, EmailNotValidError


router = APIRouter()
# db = psql_db


class User(BaseModel):
    email: str
    username: str
    # avater_img: bytes


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
#     img_url = await saveAvartarImgToStatic(file, "test")
 
#     return {
#         'url': img_url
#     }




# @router.post("/api/users")
# async def create_user(payload_: User = Depends(), avartar_img_file: UploadFile = File(...)):
#     """Create a new user"""
#     print("----------------")
#     payload = payload_.dict()
#     user = Users.create(**payload)
#     user.avatar_img_url = await saveAvartarImgToStatic(avartar_img_file, user.username)
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
    


@router.post("/api/users")
async def register(payload_: User = Depends(), avartar_img_file: UploadFile = File(...)):
    """Register user"""
    payload = payload_.dict()
    
    try:
        # validate and get info
        v = validate_email(payload["email"])
        # replace with normalized form
        payload["email"] = v["email"] 
    except EmailNotValidError:
        # email is not valid, exception message is human-readable
        return {
            "error": "Email is not valid"
        }
    
    if Users.select().where((Users.username == payload["username"]) | (Users.email == payload["email"])).exists():
        return {
            "error": "Username or email already exists"
        }
    
    user = Users.create(**payload)
    user.avatar_img_url = await saveAvartarImgToStatic(avartar_img_file, user.username)
    user.save()
    
    user = model_to_dict(user)
    return user