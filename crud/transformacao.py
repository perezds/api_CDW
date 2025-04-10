from sqlalchemy.orm import Session
from models.transformacao import Transformacao
from schemas.transformacao import TransformacaoCreate

def criar_transformacao(db: Session, transformacao: TransformacaoCreate):
    db_transformacao = Transformacao(**transformacao.dict())
    db.add(db_transformacao)
    db.commit()
    db.refresh(db_transformacao)
    return db_transformacao

def listar_transformacoes(db: Session):
    return db.query(Transformacao).all()
