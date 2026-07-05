from datetime import date as date_type
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models

MSG_CONTRACT_NOT_FOUND = "Contract not found."
MSG_DUPLICATE_CONTRACT_NUMBER = "A contract with this contract number already exists."
MSG_UNLOADING_BEFORE_LOADING = "Unloading date cannot be before loading date."
MSG_INVALID_STATUS = (
    "Invalid status. Allowed values: Loaded, Unl. & New Loading Point, Unloading, "
    "Problems, Cross the Border, Still no info, Unloaded."
)


def _next_contract_number(db: Session) -> str:
    year = date_type.today().year
    prefix = f"DSP-{year}-"
    last = (
        db.query(models.Contract)
        .filter(models.Contract.contract_number.like(f"{prefix}%"))
        .order_by(models.Contract.contract_number.desc())
        .first()
    )
    if last:
        try:
            seq = int(last.contract_number[len(prefix):]) + 1
        except (ValueError, IndexError):
            seq = 1
    else:
        seq = 1
    return f"{prefix}{seq:04d}"


def create(request: schemas.Contract, db: Session):
    contract_number = request.contract_number or _next_contract_number(db)
    existing = db.query(models.Contract).filter(
        models.Contract.contract_number == contract_number
    ).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MSG_DUPLICATE_CONTRACT_NUMBER)
    new_contract = models.Contract(
        contract_number=contract_number,
        client_name=request.client_name,
        carrier_name=request.carrier_name,
        loading_date=request.loading_date,
        unloading_date=request.unloading_date,
        status=request.status,
        loading_reference=request.loading_reference,
        unloading_reference=request.unloading_reference,
        quantity=request.quantity,
        quantity_unit=request.quantity_unit,
        item_type=request.item_type,
        price=request.price,
        comment=request.comment,
        driver_id=request.driver_id,
        driver_name=request.driver_name,
    )
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)
    return new_contract


def get_by_id(contract_id: int, db: Session):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=MSG_CONTRACT_NOT_FOUND)
    return contract


def get_all(db: Session):
    return db.query(models.Contract).order_by(models.Contract.id).all()


def get_by_status(status_value: str, db: Session):
    if status_value not in models.CONTRACT_STATUSES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MSG_INVALID_STATUS)
    return db.query(models.Contract).filter(models.Contract.status == status_value).order_by(models.Contract.id).all()


def update(contract_id: int, request: schemas.UpdateContract, db: Session):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=MSG_CONTRACT_NOT_FOUND)
    if request.contract_number is not None:
        contract.contract_number = request.contract_number
    if request.client_name is not None:
        contract.client_name = request.client_name
    if request.carrier_name is not None:
        contract.carrier_name = request.carrier_name
    if request.loading_date is not None:
        contract.loading_date = request.loading_date
    if request.unloading_date is not None:
        contract.unloading_date = request.unloading_date
    if request.status is not None:
        contract.status = request.status
    if request.loading_reference is not None:
        contract.loading_reference = request.loading_reference
    if request.unloading_reference is not None:
        contract.unloading_reference = request.unloading_reference
    if request.quantity is not None:
        contract.quantity = request.quantity
    if request.quantity_unit is not None:
        contract.quantity_unit = request.quantity_unit
    if request.item_type is not None:
        contract.item_type = request.item_type
    if request.price is not None:
        contract.price = request.price
    if request.comment is not None:
        contract.comment = request.comment
    if request.driver_id is not None:
        contract.driver_id = request.driver_id
    if request.driver_name is not None:
        contract.driver_name = request.driver_name
    if contract.unloading_date < contract.loading_date:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=MSG_UNLOADING_BEFORE_LOADING)
    db.commit()
    db.refresh(contract)
    return contract


def delete(contract_id: int, db: Session):
    contract = db.query(models.Contract).filter(models.Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=MSG_CONTRACT_NOT_FOUND)
    db.delete(contract)
    db.commit()
    return None
