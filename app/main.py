from fastapi import FastAPI
from . import models
from app.database import  engine
from .router import authentication, user, vehicle, contract
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Dispo Backend API",
    description="API for Dispo backend",
    version="1.0.0",
)

models.Base.metadata.create_all(engine)

# CORS middleware – allow frontend origin so register (JSON) preflight succeeds
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept"],
)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(vehicle.router)
app.include_router(contract.router)

