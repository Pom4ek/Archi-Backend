from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from jose import JWTError
from pydantic import ValidationError
from datetime import datetime
import time

from app.utils.password import hash_password, verify_hash_password
from app.utils.jwt import JWT, oauth2_scheme
from app.models.users import User, UserCreate, UserRead
from app.models.tokens import TokenModel, TokenPayload
from app.database.schemas import Users
from app.database.database import get_session


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserRead)
async def signup(user: UserCreate, db_session: Session = Depends(get_session)):
    
    check_user_email = db_session.query(Users).filter(Users.email == user.email).first()
    check_user_name = db_session.query(Users).filter(Users.name == user.name).first()
    
    if not check_user_email and not check_user_name:
    
        user.password = hash_password(user.password)
        
        new_user = Users(
            name=user.name,
            password=user.password,
            email=user.email,
            registered_at=datetime.utcnow()
        )
    
        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)
    
    elif not check_user_name:
        raise HTTPException(status_code=400, detail="This email is already in use.")
    else:
        raise HTTPException(status_code=400, detail="This username is already in use.")
    
    return new_user
            
    
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_session)):
    
    check_db_user = db_session.query(Users.password).filter(Users.name == form_data.username).first()
    
    if check_db_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username/Email doesn't exist."
            )
    
    if not verify_hash_password(form_data.password, check_db_user[0]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Wrong password."
            )
    
    return {
        "access_token": JWT.create_access_token(username=form_data.username),
        "refresh_token": JWT.create_refresh_token(username=form_data.username)
    }
    

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