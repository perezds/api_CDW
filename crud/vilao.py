from sqlalchemy.orm import Session
from models.vilao import Vilao
from schemas.vilao import VilaoCreate

def criar_vilao(db: Session, vilao: VilaoCreate):
    db_vilao = Vilao(**vilao.dict())
    db.add(db_vilao)
    db.commit()
    db.refresh(db_vilao)
    return db_vilao

def listar_viloes(db: Session):
    return db.query(Vilao).all()
