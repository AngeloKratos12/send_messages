from fastapi import APIRouter


router = APIRouter(
    prefix="/sign_in"
)

@router.get("/", summary="Authentification")
def sign_in():
    return {"me":"My information"}

@router.get("/forget_pass_word", summary="Mots de passe oublier")
def forget_pass():
    return {"me":"My pass_word"}