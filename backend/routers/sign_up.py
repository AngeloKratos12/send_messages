import email
from fastapi import APIRouter, Request, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from controllers.controllers import NewUserInsert
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/n_kratos/send_messages/static"), name="public")
templates = Jinja2Templates(directory="/home/n_kratos/send_messages/backend/templates")


router = APIRouter(
    prefix="/sign_up"
)

@router.get("/", summary="Authentification")
def sign_up(request: Request):
    return  templates.TemplateResponse("newcompte.html", {"request":request})

@router.get("/inscrit", summary="Authentification")
def sign_up(request: Request, nom: Optional[str] = None, prenom:Optional[str] = None, email:Optional[str] = None, password: Optional[str] = None, confirmpassword:Optional[str] = None, categorie:Optional[str] = None):
     #nom,prenom,email,password = len(nom), len(prenom), len(email), len(password)
    if (len(prenom) != 0) and (len(email) != 0) and len(password) != 0:
        if password == confirmpassword:
            newUser = NewUserInsert.put_info(nom,prenom,categorie,'0000',password,email)
            return  templates.TemplateResponse("newcompte.html", {"request":request, "inscrit":"yes"})
        else:
            password = 'wrong'
            print(password)
            return  templates.TemplateResponse("newcompte.html", {"request":request,"password":password, "inscrit":"wrong" })
    
    else:
        information = 'insuffisante'
        print(information)
        if len(prenom) == 0:
            print('prenom vide')
            prenom = 'vide'
            return  templates.TemplateResponse("newcompte.html", {"request":request, 'prenom':prenom, 'information':information})
        elif len(email) == 0:
            print('mail vide')
            email = 'vide'
            return  templates.TemplateResponse("newcompte.html", {"request":request, "email":email, 'information':information})
        else:
            password = 'vide'
            print("password vide")
            return  templates.TemplateResponse("newcompte.html", {"request":request, 'password':password, 'information':information})


@router.get("/validation", summary="Mots de passe oublier")
def forget_pass():
    return {"me":"code de validation"}
