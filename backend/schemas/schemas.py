from ast import Str
from pydantic import BaseModel, EmailStr, Field
from models.models import Categorie

class SignIn(BaseModel):
    email: EmailStr = Field()
    passWord: Str = Field(min_length=4)



class SingUp(BaseModel):
    nom: Str = Field(max_length=40)
    prenom: Str = Field(max_length=20)
    categorie: Categorie
    password: Str = Field(min_length=4)
    telephone: Str = Field(max_length=20)
