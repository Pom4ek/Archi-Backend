from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.jwt import JWT, oauth2_scheme
from jose import JWTError
from app.models.tokens import TokenPayload
from app.database.database import get_session
from app.database.schemas import Users
from sqlalchemy import or_
from sqlalchemy.orm import Session
from pydantic import ValidationError
import time


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/me")
async def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_session)):
    try:
        payload = JWT.decode_token(token)
        token_data = TokenPayload(**payload)
        if token_data.exp < time.time():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                               detail="Token expired",
                               headers={"WWW-Authenticate": "Bearer"}
                               )

    except(JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                               detail="Could not validate credentials",
                               headers={"WWW-Authenticate": "Bearer"}
                               )
    
    user = db_session.query(Users).filter(or_(Users.name == token_data.sub, Users.email == token_data.sub)).first()
    
    return user