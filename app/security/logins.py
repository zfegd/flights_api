from passlib.context import CryptContext
from admin import user


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user.UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    curruser = get_user(fake_db, username)
    if not curruser:
        return False
    if not verify_password(password, curruser.hashed_password):
        return False
    return curruser
