from models.messages import Messages
from typing import List

def add_latest_message_in_conversation(conversation_dict: dict) -> dict:
    '''Summary conversation'''
    conversation_dict['lats_message'] = Messages.get_latest_message(conversation_dict['id'])
    return conversation_dict


def format_latest_conversations(conversations: List[dict]) -> List[dict]:
    '''Format latest conversations'''
    conversations = [add_latest_message_in_conversation(conversation) for conversation in conversations]
    return conversations