from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn
import shutil
from lanceDB_manager import lanceDB_manager

app = FastAPI()
lance_manager = lanceDB_manager()



app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_image(file: UploadFile):
    save_path = f"images/{file.filename}"
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    with open(save_path, "rb") as img_file:
        lance_manager.db.open_table("images").add([{"image_uri": save_path, "image_bytes": img_file.read()}])
    return {"message": f"Image {file.filename} uploaded successfully!"}

@app.post("/search/")
async def search_image(query: str = Form(...)):
    results = lance_manager.search(query)
    return {"results": results}


# Run with `uvicorn app:app --reload`
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
