from models.messages import Messages
from models.conversations import Conversations
from models.users import Users
from typing import List, Optional
import uuid


def get_other_user_id_in_normal_conversation(
    user: uuid.UUID, members: List[uuid.UUID]
) -> uuid.UUID:
    """
    Get other user id in normal conversation
    """
    if len(members) != 2:
        raise ValueError("Members size should be 2")

    other_user_id = members[0] if members[0] != str(user) else members[1]
    return other_user_id


def add_latest_message_in_conversation(conversation_dict: dict) -> dict:
    """Summary conversation"""
    latest_message = Messages.get_messages(conversation_dict["id"], 1)
    if len(latest_message) == 0:
        conversation_dict["latest_message"] = None
    else: 
        conversation_dict["latest_message"] = latest_message[0]
    
    return conversation_dict



def format_conversation_dict(
    conversation_dict: dict, user_id: Optional[uuid.UUID] = None
) -> dict:
    """Format conversation"""
    conversation_dict = add_latest_message_in_conversation(conversation_dict)

    if conversation_dict["type"] == "Normal" and user_id is not None:
        other_user_id = get_other_user_id_in_normal_conversation(
            user_id, conversation_dict["members"]
        )
        other_user = Users.get_user_by_id(other_user_id)
        conversation_dict["name"] = other_user["username"]
        conversation_dict["avatar_img_url"] = other_user["avatar_img_url"]

    return conversation_dict


def format_conversations(
    conversations: List[dict], user_id: Optional[uuid.UUID]
) -> List[dict]:
    """Format latest conversations"""
    conversations = [
        format_conversation_dict(conversation, user_id)
        for conversation in conversations
    ]
    return conversations
