from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.mundos import MundoResponse, MundoCreate
from crud import mundos

router = APIRouter(prefix="/mundos", tags=["Mundos Mágicos"])

@router.post("/", response_model=MundoResponse)
def criar_mundo(mundo: MundoCreate, db: Session = Depends(get_db)):
    return mundos.criar_mundo(db, mundo)

@router.get("/", response_model=list[MundoResponse])
def listar_mundos(db: Session = Depends(get_db)):
    return mundos.listar_mundos(db)
