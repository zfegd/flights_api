from fastapi import Depends, FastAPI, HTTPException, status
from routers import airports
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from admin import user


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


app = FastAPI(
    title="Open Flights Project",
    description="Basic project to obtain Airport info from OpenFlights",
    version="1.0.0",
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.include_router(airports.router)


@app.get("/")
def root(token: str = Depends(oauth2_scheme)):
    return {"message": "Welcome to the Landing Page!"}


def fake_hash_password(password: str):
    return "fakehashed" + password


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user.UserInDB(**user_dict)


def fake_decode_token(token):
    curruser = get_user(fake_users_db, token)
    return curruser


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect user/password")
    curruser = user.UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == curruser.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect user/password")

    return {"access_token": curruser.username, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    curruser = fake_decode_token(token)
    if not curruser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return curruser


@app.get("/account/details")
def get_account(current_user: user.User = Depends(get_current_user)):
    return current_user
