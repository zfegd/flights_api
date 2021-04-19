from fastapi import Depends, FastAPI
from routers import airports
from fastapi.security import OAuth2PasswordBearer


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
