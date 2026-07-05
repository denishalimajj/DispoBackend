from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    return db.query(models.Carrier).order_by(models.Carrier.name).all()


def get_by_id(carrier_id: int, db: Session):
    obj = db.query(models.Carrier).filter(models.Carrier.id == carrier_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Carrier not found.")
    return obj


def create(request: schemas.CreateCarrier, db: Session):
    obj = models.Carrier(
        name=request.name,
        email=request.email,
        phone=request.phone,
        vat_number=request.vat_number,
        address=request.address,
        notes=request.notes,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(carrier_id: int, request: schemas.UpdateCarrier, db: Session):
    obj = get_by_id(carrier_id, db)
    if request.name is not None:
        obj.name = request.name
    if request.email is not None:
        obj.email = request.email
    if request.phone is not None:
        obj.phone = request.phone
    if request.vat_number is not None:
        obj.vat_number = request.vat_number
    if request.address is not None:
        obj.address = request.address
    if request.notes is not None:
        obj.notes = request.notes
    db.commit()
    db.refresh(obj)
    return obj


def delete(carrier_id: int, db: Session):
    obj = get_by_id(carrier_id, db)
    db.delete(obj)
    db.commit()
