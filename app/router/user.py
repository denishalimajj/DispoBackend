from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.oauth2 import get_current_user
from .. import database, schemas
from sqlalchemy.orm import Session
from app.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/', response_model=List[schemas.ShowUser])
def list_users(
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return user.get_all(db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return user.show_user(id, db)


@router.patch('/{id}', response_model=schemas.ShowUser)
def update_user(
    id: int,
    request: schemas.UpdateUser,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return user.update(id, request, db)


@router.delete('/{id}', status_code=204)
def delete_user(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    user.delete(id, db)
    return None
