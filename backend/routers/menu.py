from typing import Optional
from urllib import request
from fastapi import APIRouter, Form
from controllers.controllers import InfoPersoController
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/n_kratos/send_messages/static"), name="public")
templates = Jinja2Templates(directory="/home/n_kratos/send_messages/backend/templates")


router = APIRouter(
    prefix="/menu"
)


@router.post("/", summary="Boite de réception")
def reception(request : Request, user_name: str = Form(...), password: str = Form(...)):
    global user_nameV
    user_nameV = user_name
    connexion = InfoPersoController.get_info(user_name=user_name, password=password)
    if connexion == "validée":
        return templates.TemplateResponse("acceuil.html", {"request":request})
    else:
        return {"connexion":"non validée"}

@router.post("/reception", summary="Boite de réception")
def reception():

    return {"Des nouveau":"messages"}

@router.get("/message_envoye", summary="Des message envoyer")
def envoye():
    return  {"moi":"last message"}


@router.get("/new_message", summary="Envoyer un message")    
def envoye(request:Request, destination: Optional[str] = None, message: Optional[str] = None):
    print(user_nameV)
    return templates.TemplateResponse("newMessage.html", {"request":request})


@router.get("/membres", summary="Les des membres")
def membre():
    return {"membre":"All_membres"}

