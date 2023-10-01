from fastapi import FastAPI
from . import models
from app.database import  engine
from .router import authentication, user, vehicle
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

models.Base.metadata.create_all(engine)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust the origins accordingly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(vehicle.router)

