from sqlalchemy import Column, Integer, String
from app.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    tipo = Column(String, nullable=False)
    pokedex_id = Column(Integer, unique=True, nullable=False)
