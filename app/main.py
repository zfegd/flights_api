from fastapi import FastAPI
from routers import airports


app = FastAPI(
    title="Open Flights Project",
    description="Basic project to obtain Airport info from OpenFlights",
    version="1.0.0",
)


app.include_router(airports.router)


@app.get("/")
def root():
    return {"message": "Hello to the Landing Page!"}
