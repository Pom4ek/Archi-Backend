import shutil
import uvicorn

from app.routers import auth as auth_router
from app.routers import users as user_router
from app.database.database import create_db_tables
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles


create_db_tables()


app = FastAPI()


app.include_router(router=auth_router.router)
app.include_router(router=user_router.router)


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.post("/upload")
async def upload_music(uploadingtrack: UploadFile = File(...)):
    with open(f'static/{uploadingtrack.filename}','wb') as uploading_file:
        shutil.copyfileobj(uploadingtrack.file, uploading_file)