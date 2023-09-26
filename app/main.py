from fastapi import FastAPI
from . import models
from app.database import  engine
from .router import authentication, user, vehicle


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(vehicle.router)

