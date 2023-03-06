import shutil
import uvicorn

from app.routers import auth as auth_router
from app.routers import users as user_router

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.include_router(router=auth_router)
app.include_router(router=user_router)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/upload")
async def upload_music(uploadingtrack: UploadFile = File(...)):
    with open(f'static/{uploadingtrack.filename}','wb') as uploading_file:
        shutil.copyfileobj(uploadingtrack.file, uploading_file)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)