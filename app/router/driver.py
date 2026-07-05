from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.oauth2 import get_current_user
from .. import database, schemas
from app.repository import driver

router = APIRouter(prefix="/drivers", tags=["Drivers"])


@router.get("/", response_model=List[schemas.ShowDriver])
def list_drivers(
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return driver.get_all(db)


@router.post("/", response_model=schemas.ShowDriver)
def create_driver(
    request: schemas.CreateDriver,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return driver.create(request, db)


@router.patch("/{driver_id}", response_model=schemas.ShowDriver)
def update_driver(
    driver_id: int,
    request: schemas.UpdateDriver,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return driver.update(driver_id, request, db)


@router.delete("/{driver_id}", status_code=204)
def delete_driver(
    driver_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    driver.delete(driver_id, db)
    return None
