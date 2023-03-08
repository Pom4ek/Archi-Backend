from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/auth", tags=["auth"])