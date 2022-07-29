from ctypes.wintypes import CHAR
from sqlalchemy import Boolean, Column, Integer, String, Date, Time, CHAR
from db.database import Base
import enum
from sqlalchemy.dialects.mysql import ENUM





class Categorie(str, enum.Enum):
    male = "M"
    femme = "F"
    autres = "Autre"
    

class user(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(50), unique=False, index=False)
    prenom= Column(String(50), unique=False, index=False)
    categorie = Column(ENUM(Categorie))
    mail = Column(String(50))
    telephone = Column(String(15))
    password = Column(String(6))
    



class reception(Base):
    __tablename__ = "reception"

    expediteur = Column(String(50))
    id_expediteur = Column(Integer)
    destinateur = Column(String(50))
    id_destinateur = Column(Integer)
    message_ = Column(CHAR)
    date = Column(Date, index=True)
    heure = Column(Time)
    
