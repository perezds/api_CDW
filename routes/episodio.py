from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.episodio import EpisodioCreate, EpisodioResponse
from models.episodio import Episodio
from typing import List

router = APIRouter()

@router.post("/", response_model=EpisodioResponse)
def criar_episodio(episodio: EpisodioCreate, db: Session = Depends(get_db)):
    db_episodio = Episodio(**episodio.dict())
    db.add(db_episodio)
    db.commit()
    db.refresh(db_episodio)
    return db_episodio

@router.get("/", response_model=List[EpisodioResponse])
def listar_episodios(db: Session = Depends(get_db)):
    return db.query(Episodio).all()

@router.get("/{episodio_id}", response_model=EpisodioResponse)
def obter_episodio(episodio_id: int, db: Session = Depends(get_db)):
    episodio = db.query(Episodio).get(episodio_id)
    if not episodio:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    return episodio

@router.put("/{episodio_id}", response_model=EpisodioResponse)
def atualizar_episodio(episodio_id: int, dados: EpisodioCreate, db: Session = Depends(get_db)):
    episodio = db.query(Episodio).get(episodio_id)
    if not episodio:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    for key, value in dados.dict().items():
        setattr(episodio, key, value)
    db.commit()
    db.refresh(episodio)
    return episodio

@router.delete("/{episodio_id}")
def deletar_episodio(episodio_id: int, db: Session = Depends(get_db)):
    episodio = db.query(Episodio).get(episodio_id)
    if not episodio:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    db.delete(episodio)
    db.commit()
    return {"detail": "Episódio deletado com sucesso"}
