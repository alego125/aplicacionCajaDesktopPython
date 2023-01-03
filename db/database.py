from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declaramos una constante que es la que se encargara de hacer la conexion
SQLALCHEMY_DATABASE_URL = "sqlite:///caja.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
