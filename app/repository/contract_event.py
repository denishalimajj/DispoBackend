from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models


def list_by_contract(contract_id: int, db: Session):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found.")
    return (
        db.query(models.ContractEvent)
        .filter(models.ContractEvent.contract_id == contract_id)
        .order_by(models.ContractEvent.created_at.asc())
        .all()
    )


def create(contract_id: int, request: schemas.CreateContractEvent, db: Session):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contract not found.")
    event = models.ContractEvent(
        contract_id=contract_id,
        status=request.status,
        note=request.note,
        created_at=datetime.utcnow(),
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
