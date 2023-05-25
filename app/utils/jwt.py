from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class JWT():
    def __init__(self) -> None:
        pass
    
    def create_access_token(self, data):
        jwt.encode()