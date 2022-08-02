from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/menu"
)

@router.post("/reception", summary="Boite de réception")
def reception(email: str = Form(...), password: str = Form(...)):
    print(email)
    print(password)
    return {"Des nouveau":"messages"}

@router.get("/message_envoye", summary="Des message envoyer")
def envoye():
    return  {"moi":"last message"}


@router.get("/new_message", summary="Envoyer un message")
def envoye():
    return  {"moi":"new_message"}


@router.get("/membres", summary="Les des membres")
def membre():
    return {"membre":"All_membres"}