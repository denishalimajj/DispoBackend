from datetime import date as date_type, datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, Text, Float
from app.database import Base

# Contract status values (validated in schemas)
CONTRACT_STATUS_LOADED = "Loaded"
CONTRACT_STATUS_UNL_AND_NEW_LOADING = "Unl. & New Loading Point"
CONTRACT_STATUS_UNLOADING = "Unloading"
CONTRACT_STATUS_PROBLEMS = "Problems"
CONTRACT_STATUS_CROSS_THE_BORDER = "Cross the Border"
CONTRACT_STATUS_STILL_NO_INFO = "Still no info"
CONTRACT_STATUS_UNLOADED = "Unloaded"
CONTRACT_STATUSES = (
    CONTRACT_STATUS_LOADED,
    CONTRACT_STATUS_UNL_AND_NEW_LOADING,
    CONTRACT_STATUS_UNLOADING,
    CONTRACT_STATUS_PROBLEMS,
    CONTRACT_STATUS_CROSS_THE_BORDER,
    CONTRACT_STATUS_STILL_NO_INFO,
    CONTRACT_STATUS_UNLOADED,
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    mobile_phone = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    permissions = Column(String, nullable=True, default='Viewer')
    entry_date = Column(Date, nullable=True)
    expire_date = Column(Date, nullable=True)
    date_added = Column(Date, nullable=True)
    last_active = Column(Date, nullable=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    make = Column(String)
    model = Column(String)
    year = Column(String)
    color = Column(String)
    engine = Column(String)
    tableNumber = Column(String)


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contract_number = Column(String(50), unique=True, index=True, nullable=False)
    client_name = Column(String(255), nullable=False)
    carrier_name = Column(String(255), nullable=False)
    loading_date = Column(Date, nullable=False)
    unloading_date = Column(Date, nullable=False)
    status = Column(String(50), nullable=False, default=CONTRACT_STATUS_STILL_NO_INFO)
    loading_reference = Column(String(255), nullable=True)
    unloading_reference = Column(String(255), nullable=True)
    quantity = Column(String(50), nullable=True)
    quantity_unit = Column(String(10), nullable=True)
    item_type = Column(String(255), nullable=True)
    price = Column(String(50), nullable=True)
    comment = Column(Text, nullable=True)
    driver_id = Column(Integer, nullable=True)
    driver_name = Column(String(255), nullable=True)


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)


class Carrier(Base):
    __tablename__ = 'carriers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    vat_number = Column(String(100), nullable=True)
    address = Column(String(500), nullable=True)
    notes = Column(Text, nullable=True)


class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)
    license_number = Column(String(100), nullable=True)


class ContractEvent(Base):
    __tablename__ = 'contract_events'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contract_id = Column(Integer, nullable=False, index=True)
    status = Column(String(100), nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
