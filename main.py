import shutil
import uvicorn
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.post("/upload")
async def upload_music(uploadingtrack: UploadFile = File(...)):
    with open(f'static/{uploadingtrack.filename}','wb') as uploading_file:
        shutil.copyfileobj(uploadingtrack.file, uploading_file)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)