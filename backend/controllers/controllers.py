from aifc import Error
import email
from http.client import HTTPException
from unicodedata import name
from models import models
from db.database import engine
from sqlalchemy.orm import sessionmaker
from models.models import Categorie, User


models.Base.metadata.create_all(bind=engine)



class NewUserInsert:

    """
        Inserer un nouvel utilisateur
    """

    def put_info(nom, prenom, categorie,telephone, password, mail):
        Session = sessionmaker(bind=engine)
        session = Session()
        user = User(nom=nom, prenom=prenom, categorie=categorie, mail=mail, telephone=telephone, password=password)
        session.add(user)
        session.commit()


class InfoPersoController:
    """
        Identifier l'utiliateur!!
    """
    def get_info(user_name, password):
        Session = sessionmaker(bind=engine)
        session = Session()
        userV = session.query(User).filter(User.prenom == user_name)
        try:
            for row in userV:
                if row.password == password:
                    connexion = "validée"
                else:
                    connexion = "!validée"
        
            return connexion

        except Exception:
            HTTPException()
        
        