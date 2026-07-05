from typing import List, Optional

from fastapi import APIRouter, Depends, Query

from app.oauth2 import get_current_user
from .. import database, schemas
from app.repository import contract, contract_event
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"],
)


@router.post("/", response_model=schemas.ContractData)
def create_contract(
    request: schemas.Contract,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return contract.create(request, db)


@router.get("/", response_model=List[schemas.ContractData])
def list_contracts(
    status: Optional[str] = Query(None, description="Filter by contract status"),
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    if status is not None:
        return contract.get_by_status(status, db)
    return contract.get_all(db)


@router.get("/{contract_id}", response_model=schemas.ContractData)
def get_contract(
    contract_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return contract.get_by_id(contract_id, db)


@router.patch("/{contract_id}", response_model=schemas.ContractData)
def update_contract(
    contract_id: int,
    request: schemas.UpdateContract,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return contract.update(contract_id, request, db)


@router.delete("/{contract_id}", status_code=204)
def delete_contract(
    contract_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    contract.delete(contract_id, db)
    return None


@router.get("/{contract_id}/events", response_model=List[schemas.ShowContractEvent])
def list_events(
    contract_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return contract_event.list_by_contract(contract_id, db)


@router.post("/{contract_id}/events", response_model=schemas.ShowContractEvent)
def add_event(
    contract_id: int,
    request: schemas.CreateContractEvent,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserBase = Depends(get_current_user),
):
    return contract_event.create(contract_id, request, db)
