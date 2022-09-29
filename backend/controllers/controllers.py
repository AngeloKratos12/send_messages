from aifc import Error
from ast import Try
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
        Identifier l'utilisateur!!
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
        


class SendMessageController:
    """
        Mettre une message dans la BD
    """
    def putMessage(expediteur,destinateur, message):
        Session = sessionmaker(bind=engine)
        session = Session()
        id_ = session.query(User).filter(User.prenom == expediteur)
        id_expediteur = Get.getId(expediteur)
        id_destinateur = Get.getId(destinateur)

        newMessage = Reception(expediteur = expediteur, id_expediteur=id_expediteur, destinateur=destinateur,
        id_destinateur=id_destinateur,message_=message, date=datetime.datetime.today().strftime('%Y-%m-%d'), 
        heure=time.strftime('%H:%M:%S', time.localtime()))
        session.add(newMessage)
        session.commit()


class MessageRecu:
    """
        Envoyer le message vers l'interface de l'utilisateur
    """
    def reception(username):
        Session = sessionmaker(bind=engine)
        session = Session()
        id = Get.getId(username)
        message = session.query(Reception).filter(Reception.id_destinateur == id)
        listMessage = []
        for row in message:
            listMessage.append(row.message_)
        return listMessage




class Get:
    """
        Récuperer les informations
    """
    def getId(idf):
        Session = sessionmaker(bind=engine)
        session = Session()
        userV = session.query(User).filter(User.prenom == idf)
        try:
            for row in userV:
                id = row.id
            return id

        except Exception:
            HTTPException()
    
    def user(prenom):
        Session = sessionmaker(bind=engine)
        session = Session()
        idUser = Get.getId(prenom)
        userv = session.query(Reception).filter(Reception.id_destinateur == idUser)
        listuser = []
        setiduser = []
        try:
            for row in userv:
                setiduser.append(row.id_expediteur)
            
            setiduser = set(setiduser)
            for i in setiduser:
                user = session.query(User).filter(User.id == i)
                for row in user:
                    listuser.append(row.prenom)
            return listuser
                

        except Exception:
            HTTPException()


