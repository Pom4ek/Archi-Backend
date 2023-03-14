from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.utils import hash_password, verify_hash_password
from app.models.users import User, UserCreate, UserRead
from app.database.schemas import Users
from app.database.database import get_session


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserRead)
async def signup(user: UserCreate, session: Session = Depends(get_session)):
    
    check_user_email = session.query(Users).filter(Users.email == user.email).first()
    check_user_name = session.query(Users).filter(Users.name == user.name).first()
    
    if not check_user_email and not check_user_name:
        
        user.password = hash_password(user.password)
        
        new_user = Users(
            name=user.name,
            password=user.password,
            email=user.email
        )
    
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
    elif not check_user_name:
        raise HTTPException(status_code=400, detail="This email is already in use")
    else:
        raise HTTPException(status_code=400, detail="This username is already in use")
    
    return new_user
            
    
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    
    check_db_user = session.execute(select(Users.name & Users.email).where(Users.name == form_data.username))
    
    
    return None