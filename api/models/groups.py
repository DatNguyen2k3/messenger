from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from .conversations import Conversations
from playhouse.postgres_ext import ArrayField



class Groups(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    conversation = p.ForeignKeyField(Conversations, backref='conversation')
    name = p.CharField(max_length=255)
    admins = ArrayField(p.TextField, default=[])