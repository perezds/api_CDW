from sqlalchemy.orm import Session
from models.mundos import MundoMagico
from schemas.mundos import MundoCreate

def criar_mundo(db: Session, mundo: MundoCreate):
    db_mundo = MundoMagico(**mundo.dict())
    db.add(db_mundo)
    db.commit()
    db.refresh(db_mundo)
    return db_mundo

def listar_mundos(db: Session):
    return db.query(MundoMagico).all()
