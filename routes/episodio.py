from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.episodio import EpisodioCreate, EpisodioResponse
from crud import episodio as crud_episodio

router = APIRouter()

@router.post("/", response_model=EpisodioResponse)
def criar_episodio(episodio: EpisodioCreate, db: Session = Depends(get_db)):
    return crud_episodio.criar_episodio(db, episodio)

@router.get("/", response_model=list[EpisodioResponse])
def listar_episodios(db: Session = Depends(get_db)):
    return crud_episodio.listar_episodios(db)
