from fastapi import FastAPI, APIRouter


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup",)
def signup():
    return None
    