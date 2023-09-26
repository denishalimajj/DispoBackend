from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, hashing


def createVehicle(request: schemas.Vehicle, db: Session):
    new_vehicle = models.Vehicle(type = request.type, make = request.make ,model = request.model, year = request.year,color = request.color,engine = request.engine, tableNumber = request.tableNumber)
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

def show_vehicle(id:int, db: Session):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == id).first()
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vehicle with id {id} could not be found")
    return vehicle

def show_all_vehicles(db:Session):
    showall = db.query(models.Vehicle).all()
    if not showall:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is not a vehicle registerd. Please wait until it's registered")
    return showall

def update_vehicle(vehicle_id: int, request: schemas.UpdateVehicle, db: Session):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail=f"Vehicle with id {vehicle_id} not found")

    if request.type:
        vehicle.type = request.type
    if request.make:
        vehicle.make = request.make
    if request.model:
        vehicle.model = request.model
    if request.year:
        vehicle.year = request.year
    if request.color:
        vehicle.color = request.color
    if request.engine:
        vehicle.engine = request.engine
    if request.tableNumber:
        vehicle.tableNumber = request.tableNumber
    
    db.commit()
    db.refresh(vehicle)
    return vehicle  