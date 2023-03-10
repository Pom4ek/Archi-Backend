from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.utils import hash_password, verify_hash_password
from app.models.users import User, UserCreate, UserRead
from app.database.schemas import Users
from app.database.database import get_session, engine


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserRead)
async def signup(user: UserCreate):
    
    session = get_session()
    check_user_db = session.execute(select(Users.email).where(Users.email == user.email))
    fetched_email = None
    
    for row in check_user_db:
        fetched_email = row[0]
    
    if fetched_email is not None:
        raise HTTPException(status_code=400,detail="This email is already in use")
    
    user.password = hash_password(user.password)
    new_user = Users(
        name=user.name,
        password=user.password,
        email=user.email
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
            
    
    
@router.post("/login")
async def login():
    return None