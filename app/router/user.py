from fastapi import APIRouter, Depends, HTTPException, status

from app.oauth2 import get_current_user
from .. import database, schemas
from sqlalchemy.orm import Session
from app.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', response_model=schemas.UserBase)
def create_user(request:schemas.User,db: Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model= schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db),get_current_user: schemas.User = Depends(get_current_user)):
    return user.show_user(id, db)