from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str 
    
class UserBase(BaseModel):
    id: int
    name: str
    email: str         
    
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True 
        
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
    id:int
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





                
        