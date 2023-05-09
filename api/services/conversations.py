

def summary_conversation(conversation_dict: dict) -> dict:
    '''Summary conversation'''
    conversation_dict['created_by'] = conversation_dict['created_by']['id']
    conversation_dict['modified_by'] = conversation_dict['modified_by']['id']
    
    return conversation_dict