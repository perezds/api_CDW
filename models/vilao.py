from sqlalchemy import Column, Integer, String
from core.database import Base

class Vilao(Base):
    __tablename__ = "viloes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    ameaca_nivel = Column(String, nullable=True)  
