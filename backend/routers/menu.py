from fastapi import APIRouter

router = APIRouter(
    prefix="/menu"
)

@router.get("/reception", summary="Boite de réception")
def reception():
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