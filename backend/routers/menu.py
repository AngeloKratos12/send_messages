from email import message
from typing import Optional
from urllib import request
from fastapi import APIRouter, Form
from controllers.controllers import InfoPersoController,   SendMessageController, MessageRecu, Get
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/n_kratos/send_messages/static"), name="public")
templates = Jinja2Templates(directory="/home/n_kratos/send_messages/backend/templates")


router = APIRouter(
    prefix="/menu"
)


@router.post("/", summary="Boite de réception")
def sign(request : Request, user_name: str = Form(...), password: str = Form(...)):
    connexion = InfoPersoController.get_info(user_name=user_name, password=password)
    if connexion == "validée":
        return templates.TemplateResponse("acceuil.html", {"request":request})
    else:
        return {"connexion":"non validée"}

@router.get("/reception", summary="Boite de réception")
def reception(request: Request, username : str):
    message = MessageRecu.reception(username)
    print(message)
    name = Get.user(username)
    return templates.TemplateResponse("reception.html", {"request":request, "message":message, "len":len(message),"nameuser":name, "lenuser":len(name), "message":message })

@router.get("/reception/messagerecu", summary="Boite de réception")
def message(request: Request):
    
    return templates.TemplateResponse("messagerecus.html", {"request":request})




@router.get("/message_envoye", summary="Des message envoyer")
def envoye():
    return  {"moi":"last message"}


@router.get("/new_message", summary="Envoyer un message")    
def envoye(request:Request):
    return templates.TemplateResponse("newMessage.html", {"request":request})


@router.post("/sendmessage", summary="Envoyer un message")    
async def envoye(request:Request, file:UploadFile=File(description="file as uploadfile"),destination:str=Form(...)):

    
    print(destination)
    ext_doc = ['.docx','.pdf','.pttxt','.xlsx']
    ext_img = ['.png','.jpeg','.jpg']
    ext_audio = ['.mp3','.ma4']
    ext_video = ['.mp4','.avi']
    filename = file.filename
    if len(filename) != 0 :
        content_type = file.content_type
        file = file.file
        content_file = file.read()
        print(len(filename))
        for index in range(len(filename)):
            if filename[index] == '.':
                extension = filename[index:]
                break
                #print("ext",extension)
            else:
                pass
        
        if extension in ext_doc:
            FILEPATH = './medias/DOCS/'
        elif extension in ext_img:
            FILEPATH = './medias/images/'
        elif extension in ext_audio:
            FILEPATH = './medias/audios/'
        elif extension in ext_video:
            FILEPATH = './medias/videos/'
        else:
            FILEPATH = './medias/autres/'
        
        with open(FILEPATH + filename, "wb") as file:
            file.write(content_file)
        file.close()
    #send = SendMessageController.putMessage(username,destination,message)
    
    return templates.TemplateResponse("newMessage.html", {"request":request})


@router.get("/membres", summary="Les des membres")
def membre():
    return {"membre":"All_membres"}

