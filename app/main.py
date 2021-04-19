from fastapi import Depends, FastAPI, HTTPException, status
from routers import airports
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from admin import user, tokens
from jose import JWTError, jwt
from datetime import timedelta
from security import userbase, authorization, logins


app = FastAPI(
    title="Open Flights Project",
    description="Basic project to obtain Airport info from OpenFlights",
    version="1.0.0",
)


app.include_router(airports.router)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
def root(token: str = Depends(oauth2_scheme)):
    return {"message": "Welcome to the Landing Page!"}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    curruser = logins.authenticate_user(
                    userbase.fake_users_db, form_data.username,
                    form_data.password)
    if not curruser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
                            minutes=authorization.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authorization.create_access_token(
        data={"sub": curruser.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, authorization.SECRET_KEY,
                             algorithms=[authorization.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = tokens.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    curruser = logins.get_user(userbase.fake_users_db,
                               username=token_data.username)
    if curruser is None:
        raise credentials_exception
    return curruser


@app.get("/account/details")
def get_account(current_user: user.User = Depends(get_current_user)):
    return current_user
