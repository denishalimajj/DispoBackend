from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:denis1234?@localhost:5432/DispoDB'
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine,autoflush=False, autocommit= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    