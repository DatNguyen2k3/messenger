from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from playhouse.postgres_ext import ArrayField


def members_validator(value):
    for member in value:
        if not Users.select().where(Users.id == member).exists():
            raise ValueError('Member does not exist')
            
            
class Conversations(PeeWeeBaseModel):
    CONVERSATION_TYPES = (
        ('Normal', 'Normal'),
        ('Group', 'Group')
    )       
            
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    created_by = p.ForeignKeyField(Users, backref='created_user')
    created_at = p.DateTimeField(default=datetime.datetime.now)
    modified_by = p.ForeignKeyField(Users, backref='modified_user')    
    modified_at = p.DateTimeField(default=datetime.datetime.now)
    type = p.CharField(choices=CONVERSATION_TYPES)
    members = ArrayField(p.TextField, default=[])

            