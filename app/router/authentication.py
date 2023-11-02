from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .. import schemas, database, models, hashing, token
from sqlalchemy.orm import Session
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login = Depends(OAuth2PasswordRequestForm), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    if not  hashing.Hash.verify(user.password, request.password):
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid password")
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}