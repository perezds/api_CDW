from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Winx(Base):
    __tablename__ = "winx"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    poder_principal = Column(String)
    planeta_origem = Column(String)
    transformacao_favorita = Column(String)
    mundo_id = Column(Integer, ForeignKey("mundos_magicos.id"))

    mundo = relationship("MundoMagico", back_populates="fadas")
