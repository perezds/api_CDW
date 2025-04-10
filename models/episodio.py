from sqlalchemy import Column, Integer, String
from core.database import Base

class Episodio(Base):
    __tablename__ = "episodios"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, nullable=False)
    temporada = Column(Integer, nullable=False)
    titulo = Column(String, nullable=False)
    sinopse = Column(String, nullable=True)
