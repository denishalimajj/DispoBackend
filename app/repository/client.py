from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all(db: Session):
    return db.query(models.Client).order_by(models.Client.name).all()


def get_by_id(client_id: int, db: Session):
    obj = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found.")
    return obj


def create(request: schemas.CreateClient, db: Session):
    obj = models.Client(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address,
        notes=request.notes,
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(client_id: int, request: schemas.UpdateClient, db: Session):
    obj = get_by_id(client_id, db)
    if request.name is not None:
        obj.name = request.name
    if request.email is not None:
        obj.email = request.email
    if request.phone is not None:
        obj.phone = request.phone
    if request.address is not None:
        obj.address = request.address
    if request.notes is not None:
        obj.notes = request.notes
    db.commit()
    db.refresh(obj)
    return obj


def delete(client_id: int, db: Session):
    obj = get_by_id(client_id, db)
    db.delete(obj)
    db.commit()
