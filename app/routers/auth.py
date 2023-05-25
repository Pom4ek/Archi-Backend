from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.utils import hash_password, verify_hash_password
from app.models.users import User, UserCreate, UserRead
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
            email=user.email
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
    
    check_db_user = db_session.query(Users).filter(or_(Users.name == form_data.username, Users.email == form_data.username))
    
    if check_db_user is None:
        raise HTTPException(status_code=400, detail="Username/Email doesn't exist.")
    
    if not verify_hash_password(form_data.password, check_db_user.password):
        raise HTTPException(status_code=400, detail="Wrong password.")
    
    
    
    
    return None