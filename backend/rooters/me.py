from fastapi import APIRouter


router = APIRouter(
    prefix="/me"
)
@router.get("/", summary="Savoir un peu plus sur moi!!")
def me():
    return {"me":"information"}