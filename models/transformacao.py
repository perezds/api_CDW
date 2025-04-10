from sqlalchemy import Column, Integer, String
from core.database import Base

class Transformacao(Base):
    __tablename__ = "transformacoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    nivel_magico = Column(String, nullable=True)
