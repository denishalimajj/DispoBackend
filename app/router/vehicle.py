
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.oauth2 import get_current_user
from .. import database, schemas
from sqlalchemy.orm import Session
from app.repository import vehicle

router = APIRouter(
    prefix="/vehicle",
    tags=['Vehicles']
)

@router.post('/', response_model=schemas.VehicleData)
def create_vehicle(request:schemas.Vehicle, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return vehicle.createVehicle(request, db)

@router.get('/{id}', response_model= schemas.VehicleData)
def get_vehicle(id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return vehicle.show_vehicle(id, db)

@router.get('/',response_model=List[(schemas.VehicleData)])
def get_all(db:Session = Depends(database.get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return vehicle.show_all_vehicles(db)

@router.patch('/{id}', response_model= schemas.VehicleData)
def update(id: int,request: schemas.UpdateVehicle ,db:Session = Depends(database.get_db), get_current_user: schemas.User = Depends(get_current_user)):
    return vehicle.update_vehicle(id,request,db)