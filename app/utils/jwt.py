from jose import jwt, JWTError
from app.config import (
    SECRET, 
    SECRET_ALGORITHM, 
    ACCESS_TOKEN_EXPIRE_MINUTES, 
    REFRESH_TOKEN_EXPIRE_DAYS
)
from datetime import timedelta
import time
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", scheme_name="JWT")
        

class JWT():
    def __init__(self) -> None:
        pass
    
    
    def create_access_token(username: str) -> dict[str, str]:
        payload = {
            "sub": username,
            "exp": time.time() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES).seconds
        }
        access_token = jwt.encode(claims=payload, key=SECRET, algorithm=SECRET_ALGORITHM)
        return access_token
    
    
    def create_refresh_token(username: str) -> dict[str, str]:
        payload = {
            "sub": username,
            "exp": time.time() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS).seconds,
        }
        refresh_token = jwt.encode(claims=payload, key=SECRET, algorithm=SECRET_ALGORITHM)
        return refresh_token
    
    
    def decode_token(token: str):
        return jwt.decode(token, SECRET, SECRET_ALGORITHM)
    
    