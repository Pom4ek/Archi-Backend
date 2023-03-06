from fastapi import FastAPI, APIRouter
from app.utils import hash_password, verify_hash_password
from app.models.users import User, UserCreate


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def signup():
    return None
    
    
@router.post("/login")
async def login():
    return None