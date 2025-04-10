from sqlalchemy.orm import Session
from models.poder import Poder
from schemas.poder import PoderCreate

def criar_poder(db: Session, poder: PoderCreate):
    db_poder = Poder(**poder.dict())
    db.add(db_poder)
    db.commit()
    db.refresh(db_poder)
    return db_poder

def listar_poderes(db: Session):
    return db.query(Poder).all()
