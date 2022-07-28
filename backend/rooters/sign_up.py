from fastapi import APIRouter


router = APIRouter(
    prefix="/sign_up"
)

@router.get("/", summary="Authentification")
def sign_up():
    return {"me":"My information"}

@router.get("/validation", summary="Mots de passe oublier")
def forget_pass():
    return {"me":"code de validation"}