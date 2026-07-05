from datetime import date, datetime
from typing import List, Literal, Optional
from pydantic import BaseModel, model_validator


class User(BaseModel):
    name: str
    email: str
    password: str
    mobile_phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    permissions: Optional[str] = "Viewer"
    entry_date: Optional[date] = None
    expire_date: Optional[date] = None


class UserBase(BaseModel):
    id: int
    name: str
    email: str


class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    mobile_phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    permissions: Optional[str] = None
    entry_date: Optional[date] = None
    expire_date: Optional[date] = None
    date_added: Optional[date] = None
    last_active: Optional[date] = None

    class Config:
        from_attributes = True


class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    mobile_phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    permissions: Optional[str] = None
    entry_date: Optional[date] = None
    expire_date: Optional[date] = None


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Vehicle(BaseModel):
    type: str
    make: str
    model: str
    year: str
    color: str
    engine: str
    tableNumber: str


class VehicleData(BaseModel):
    id: int
    type: str
    make: str
    model: str
    year: str
    color: str
    engine: str
    tableNumber: str


class UpdateVehicle(BaseModel):
    type: Optional[str]
    make: Optional[str]
    model: Optional[str]
    year: Optional[str]
    color: Optional[str]
    engine: Optional[str]
    tableNumber: Optional[str]


# Contract status values (must match models.CONTRACT_STATUSES)
ContractStatusLiteral = Literal[
    "Loaded",
    "Unl. & New Loading Point",
    "Unloading",
    "Problems",
    "Cross the Border",
    "Still no info",
    "Unloaded",
]


class Contract(BaseModel):
    contract_number: Optional[str] = None
    client_name: str
    carrier_name: str
    loading_date: date
    unloading_date: date
    status: ContractStatusLiteral = "Still no info"
    loading_reference: Optional[str] = None
    unloading_reference: Optional[str] = None
    quantity: Optional[str] = None
    quantity_unit: Optional[str] = None
    item_type: Optional[str] = None
    price: Optional[str] = None
    comment: Optional[str] = None
    driver_id: Optional[int] = None
    driver_name: Optional[str] = None

    @model_validator(mode="after")
    def unloading_date_not_before_loading(self):
        if self.unloading_date < self.loading_date:
            raise ValueError("Unloading date cannot be before loading date.")
        return self


class ContractData(BaseModel):
    id: int
    contract_number: str
    client_name: str
    carrier_name: str
    loading_date: date
    unloading_date: date
    status: str
    loading_reference: Optional[str] = None
    unloading_reference: Optional[str] = None
    quantity: Optional[str] = None
    quantity_unit: Optional[str] = None
    item_type: Optional[str] = None
    price: Optional[str] = None
    comment: Optional[str] = None
    driver_id: Optional[int] = None
    driver_name: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateContract(BaseModel):
    contract_number: Optional[str] = None
    client_name: Optional[str] = None
    carrier_name: Optional[str] = None
    loading_date: Optional[date] = None
    unloading_date: Optional[date] = None
    status: Optional[ContractStatusLiteral] = None
    loading_reference: Optional[str] = None
    unloading_reference: Optional[str] = None
    quantity: Optional[str] = None
    quantity_unit: Optional[str] = None
    item_type: Optional[str] = None
    price: Optional[str] = None
    comment: Optional[str] = None
    driver_id: Optional[int] = None
    driver_name: Optional[str] = None

    @model_validator(mode="after")
    def unloading_date_not_before_loading(self):
        if self.loading_date is not None and self.unloading_date is not None:
            if self.unloading_date < self.loading_date:
                raise ValueError("Unloading date cannot be before loading date.")
        return self


# ── Client ──────────────────────────────────────────────────────────────────

class CreateClient(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None


class ShowClient(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateClient(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None


# ── Carrier ──────────────────────────────────────────────────────────────────

class CreateCarrier(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    vat_number: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None


class ShowCarrier(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    vat_number: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateCarrier(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    vat_number: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None


# ── Driver ───────────────────────────────────────────────────────────────────

class CreateDriver(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    license_number: Optional[str] = None


class ShowDriver(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    license_number: Optional[str] = None

    class Config:
        from_attributes = True


class UpdateDriver(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    license_number: Optional[str] = None


# ── Contract Events ──────────────────────────────────────────────────────────

class CreateContractEvent(BaseModel):
    status: str
    note: Optional[str] = None


class ShowContractEvent(BaseModel):
    id: int
    contract_id: int
    status: str
    note: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
