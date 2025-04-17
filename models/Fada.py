# models/fada.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Fada(Base):
    __tablename__ = "fadas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    imagem_url = Column(String, nullable=True)  

    winx_id = Column(Integer, ForeignKey("winx.id")) 
    winx = relationship("Winx", back_populates="fadas")  

    poderes = relationship("Poder", back_populates="fada")
    episodios = relationship("Episodio", back_populates="fada")
    transformacoes = relationship("Transformacao", back_populates="fada")
