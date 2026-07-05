from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    return db.query(models.Driver).order_by(models.Driver.name).all()


def get_by_id(driver_id: int, db: Session):
    obj = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Driver not found.")
    return obj


def create(request: schemas.CreateDriver, db: Session):
    obj = models.Driver(
        name=request.name,
        email=request.email,
        phone=request.phone,
        license_number=request.license_number,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(driver_id: int, request: schemas.UpdateDriver, db: Session):
    obj = get_by_id(driver_id, db)
    if request.name is not None:
        obj.name = request.name
    if request.email is not None:
        obj.email = request.email
    if request.phone is not None:
        obj.phone = request.phone
    if request.license_number is not None:
        obj.license_number = request.license_number
    db.commit()
    db.refresh(obj)
    return obj


def delete(driver_id: int, db: Session):
    obj = get_by_id(driver_id, db)
    db.delete(obj)
    db.commit()
