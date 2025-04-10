from sqlalchemy import Column, Integer, String
from core.database import Base

class Winx(Base):
    __tablename__ = "winx"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    poder = Column(String)
    planeta_origem = Column(String)
    transformacao_favorita = Column(String)
