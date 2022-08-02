from fastapi import APIRouter


router = APIRouter(
    prefix="/sign_in"
)

@router.get("/forget_pass_word", summary="Mots de passe oublier")
def forget_pass():
    return {"me":"My pass_word"}