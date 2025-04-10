from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class MundoMagico(Base):
    __tablename__ = "mundos_magicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    descricao = Column(String)
    habitado_por = Column(String)

    fadas = relationship("Winx", back_populates="mundo", cascade="all, delete-orphan")
