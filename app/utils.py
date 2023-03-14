from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def hash_password(plain_password: str):
    return password_context.hash(plain_password)


def verify_hash_password(plain_password: str, hashed_password: str):
    return password_context.verify(plain_password, hashed_password)


# def create_jwt_token():
#     jwt.decode
#     return None

