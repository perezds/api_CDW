from sqlalchemy.orm import Session
from models.transformacoes import Transformacoes
from schemas.transformacoes import TransformacaoCreate

def criar_transformacao(db: Session, transformacao: TransformacaoCreate):
    nova_transformacao = Transformacoes(**transformacao.dict())
    db.add(nova_transformacao)
    db.commit()
    db.refresh(nova_transformacao)
    return nova_transformacao

def listar_transformacoes(db: Session):
    return db.query(Transformacoes).all()
