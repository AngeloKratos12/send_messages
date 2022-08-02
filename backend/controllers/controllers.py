import email
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
    def get_info(email, password):
        Session = sessionmaker(bind=engine)
        session = Session()