from decimal import Overflow
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://angelo:angelo@localhost:3306/sms"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size = 20, max_overflow = 0
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    """
        DESC: Création d'une session pour la base de donnée
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()