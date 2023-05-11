from . import PeeWeeBaseModel
import peewee as p
import uuid
import datetime
from .users import Users
from .conversations import Conversations
from schemas.message import Message
from playhouse.shortcuts import model_to_dict
from typing import List
from pydantic import PositiveInt


class Messages(PeeWeeBaseModel):
    id = p.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    from_user = p.ForeignKeyField(Users, backref="from_user")
    to_conversation = p.ForeignKeyField(Conversations, backref="to_conversation")
    created_at = p.DateTimeField(default=datetime.datetime.now)
    modified_at = p.DateTimeField(default=datetime.datetime.now)
    is_deleted = p.BooleanField(default=False)
    content = p.TextField()

    @classmethod
    def create_message(cls, payload_: Message) -> dict:
        """Create message"""
        payload = payload_.dict()

        conversation = Conversations.get_by_id(payload["to_conversation"])
        if str(payload["from_user"]) not in conversation.members:
            raise ValueError("User is not a member of the conversation")

        # Update conversation modified_at and modified_by
        conversation.modified_at = datetime.datetime.now()
        conversation.modified_by = payload["from_user"]
        conversation.save()

        message = cls.create(**payload)
        message_dict = model_to_dict(message)
        return message_dict

    @classmethod
    def get_messages(cls, conversation_id: uuid.UUID, limit:  PositiveInt = 20) -> List[dict]:
        """
        Get latest messages
        """
        
        messages = (
            Messages.select()
            .where(Messages.to_conversation == conversation_id)
            .order_by(Messages.created_at.desc())
            .limit(limit)
        )

        messages_dict = [model_to_dict(message) for message in messages]
        return messages_dict