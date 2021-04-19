from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    # password: str


class UserInDB(User):
    hashed_password: str
