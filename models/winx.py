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

    mundo = relationship("MundoMagico", back_populates="fadas")
    transformacoes = relationship("Transformacao", back_populates="fada", cascade="all, delete-orphan")
