from sqlalchemy import Column, Integer, String
from core.database import Base

class Poder(Base):
    __tablename__ = "poderes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
