import re

ALPHANUM = re.compile('^[a-zA-Z0-9_.]+$')


def is_valid_username(username: str) -> bool:
    """
    Check if username is valid
    """
    
    if ALPHANUM.match(username) is None:
        return False

    return True

