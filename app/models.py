from sqlalchemy import Column, Integer, String
from app.database import Base



class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


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

    
