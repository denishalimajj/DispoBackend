from datetime import date
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, hashing


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
        mobile_phone=request.mobile_phone,
        date_of_birth=request.date_of_birth,
        gender=request.gender,
        permissions=request.permissions or 'Viewer',
        entry_date=request.entry_date,
        expire_date=request.expire_date,
        date_added=date.today(),
        last_active=date.today(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session):
    return db.query(models.User).order_by(models.User.id).all()


def show_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} could not be found")
    return user


def update(id: int, request: schemas.UpdateUser, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} could not be found")
    if request.name is not None:
        user.name = request.name
    if request.email is not None:
        user.email = request.email
    if request.mobile_phone is not None:
        user.mobile_phone = request.mobile_phone
    if request.date_of_birth is not None:
        user.date_of_birth = request.date_of_birth
    if request.gender is not None:
        user.gender = request.gender
    if request.permissions is not None:
        user.permissions = request.permissions
    if request.entry_date is not None:
        user.entry_date = request.entry_date
    if request.expire_date is not None:
        user.expire_date = request.expire_date
    user.last_active = date.today()
    db.commit()
    db.refresh(user)
    return user


def delete(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} could not be found")
    db.delete(user)
    db.commit()
    return None
