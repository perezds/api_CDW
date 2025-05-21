from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Transformacao(Base):
    __tablename__ = "transformacoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    nivel_magico = Column(String, nullable=True)
    winx_id = Column(Integer, ForeignKey("winx.id"))

    fada = relationship("Winx", back_populates="transformacoes")
