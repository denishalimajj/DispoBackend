from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.oauth2 import get_current_user
from .. import database, schemas
from app.repository import carrier

router = APIRouter(prefix="/carriers", tags=["Carriers"])


@router.get("/", response_model=List[schemas.ShowCarrier])
def list_carriers(
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return carrier.get_all(db)


@router.post("/", response_model=schemas.ShowCarrier)
def create_carrier(
    request: schemas.CreateCarrier,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return carrier.create(request, db)


@router.patch("/{carrier_id}", response_model=schemas.ShowCarrier)
def update_carrier(
    carrier_id: int,
    request: schemas.UpdateCarrier,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return carrier.update(carrier_id, request, db)


@router.delete("/{carrier_id}", status_code=204)
def delete_carrier(
    carrier_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    carrier.delete(carrier_id, db)
    return None
