""" main module """
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index():
    """ index page """
    return {"NLP": "App"}


@app.get("/item") ##, response_class=HTMLResponse)
async def read_item(): ##request: Request):
    """ read_item """
    return templates.TemplateResponse("item.html", {})
