from aifc import Error
from datetime import date
import email
from http.client import HTTPException
from unicodedata import name
from models import models
from db.database import engine
from sqlalchemy.orm import sessionmaker
from models.models import Categorie, User, Reception
import time
import datetime 


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
        


class EnvoieMessageController:
    """
        Mettre une message dans la BD
    """
    def putMessage(expediteur,destinateur, message):
        Session = sessionmaker(bind=engine)
        session = Session()
        id_ = session.query(User.filter(User.prenom == expediteur))
        id_destinateur = None
        id_expediteur = None
        time = time.strftime('%H:%M:%S', time.localtime())
        try:
            for row in id_:
                row.id == id_expediteur

        except Exception:
            HTTPException()
        
        id_ = session.query(User.filter(User.prenom == destinateur))
        try:
            for row in id_:
                row.id == id_destinateur

        except Exception:
            HTTPException()

        newMessage = Reception(expediteur = expediteur, id_expediteur=id_expediteur, destinateur=destinateur,
        id_destinateur=id_destinateur,message=message, date=datetime.datetime.today().strftime('%Y-%m-%d'), time=time)






class Reception(Base):
    __tablename__ = "reception"

    id = Column(Integer, primary_key=True, index=True)
    expediteur = Column(String(50))
    id_expediteur = Column(Integer)
    destinateur = Column(String(50))
    id_destinateur = Column(Integer)
    message_ = Column(CHAR)
    date = Column(Date, index=True)
    heure = Column(Time)