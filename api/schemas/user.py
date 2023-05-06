from pydantic import BaseModel


class User(BaseModel):
    """
    User model
    """

    email: str
    username: str
