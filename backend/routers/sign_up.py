from fastapi import APIRouter, Request, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/n_kratos/send_messages/static"), name="public")
templates = Jinja2Templates(directory="/home/n_kratos/send_messages/backend/templates")


router = APIRouter(
    prefix="/sign_up"
)

@router.get("/", summary="Authentification")
def sign_up(request: Request):
    return  templates.TemplateResponse("newcompte.html", {"request":request})

@router.get("/validation", summary="Mots de passe oublier")
def forget_pass():
    return {"me":"code de validation"}
