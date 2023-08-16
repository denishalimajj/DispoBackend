from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str 
    
class UserBase(BaseModel):
    name: str
    email: str
            
    
class ShowUser(BaseModel):
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
                
        