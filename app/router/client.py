from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.oauth2 import get_current_user
from .. import database, schemas
from app.repository import client

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.get("/", response_model=List[schemas.ShowClient])
def list_clients(
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return client.get_all(db)


@router.post("/", response_model=schemas.ShowClient)
def create_client(
    request: schemas.CreateClient,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return client.create(request, db)


@router.patch("/{client_id}", response_model=schemas.ShowClient)
def update_client(
    client_id: int,
    request: schemas.UpdateClient,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return client.update(client_id, request, db)


@router.delete("/{client_id}", status_code=204)
def delete_client(
    client_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    client.delete(client_id, db)
    return None
