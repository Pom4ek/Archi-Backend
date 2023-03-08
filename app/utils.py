from passlib.context import CryptContext
from jose import jwt

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str):
    return password_context.hash(plain_password)


def verify_hash_password(plain_password: str, hashed_password: str):
    return password_context.verify(plain_password, hashed_password)


def create_jwt_token():
    encoded_jwt_token = 1
    return encoded_jwt_token

