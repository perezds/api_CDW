# models/winx.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Winx(Base):
    __tablename__ = "winx"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    poder_principal = Column(String, nullable=False)
    transformacao_favorita = Column(String, nullable=False)
    planeta_origem = Column(String, nullable=False)
    mundo_id = Column(Integer, ForeignKey("mundos_magicos.id"))

<<<<<<< HEAD
    mundo = relationship("MundoMagico", back_populates="fadas")
    transformacoes = relationship("Transformacao", back_populates="fada", cascade="all, delete-orphan")
=======
    mundo = relationship("MundoMagico", back_populates="winx")  
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
