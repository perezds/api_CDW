from sqlalchemy.orm import Session
from models.episodio import Episodio
from schemas.episodio import EpisodioCreate

def criar_episodio(db: Session, episodio: EpisodioCreate):
    db_episodio = Episodio(**episodio.dict())
    db.add(db_episodio)
    db.commit()
    db.refresh(db_episodio)
    return db_episodio

def listar_episodios(db: Session):
    return db.query(Episodio).all()
