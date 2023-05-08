import uuid
from email_validator import validate_email, EmailNotValidError

def convert_file_name(file, new_file_name):
    """
    Convert file name to new file name
    """
    old_file_name = file.filename
    tail_index = old_file_name.rfind(".")
    return new_file_name + old_file_name[tail_index:]


def is_valid_uuid(val):
    '''
    Check if val is valid uuid
    '''
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
    

def is_valid_email(email):
    '''
    Check if email is valid
    '''
    try: 
        validate_email(email)
        return True
    except EmailNotValidError:
        return False