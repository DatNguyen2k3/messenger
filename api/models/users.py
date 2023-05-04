from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime


class Users(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    username = p.CharField(max_length=255, unique=True)
    email = p.CharField(max_length=255, unique=True)
    avatar_img_url = p.CharField(max_length=1000, null=True)
    created_at = p.DateTimeField(default= datetime.datetime.now)
    modified_at = p.DateTimeField(default= datetime.datetime.now)
    
    