from pydantic import BaseModel


class TokenPayload(BaseModel):
    sub: str
    exp: float
    

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str