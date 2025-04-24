from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.mundos import MundoMagico
from schemas.mundos import MundoResponse, MundoCreate

router = APIRouter()

@router.post("/", response_model=MundoResponse)
def criar_mundo(mundo :MundoCreate, db: Session = Depends(get_db)):
    db_mundo = mundo(**mundo.dict())
    db.add(db_mundo)
    db.commit()
    db.refresh(db_mundo)
    return db_mundo

@router.get("/", response_model=List[MundoResponse])
def listar_mundos(db: Session = Depends(get_db)):
    return db.query(MundoMagico).all()

@router.get("/{mundo_id}", response_model=MundoResponse)
def obter_mundo(mundo_id: int, db: Session = Depends(get_db)):
    mundo = db.query(MundoMagico).get(mundo_id)
    if not mundo:
        raise HTTPException(status_code=404, detail="Mundo não encontrado")
    return mundo

@router.put("/{mundo_id}", response_model=MundoResponse)
def atualizar_mundo(mundo_id: int, dados: MundoCreate, db: Session = Depends(get_db)):
    mundo = db.query(MundoMagico).get(mundo_id)
    if not mundo:
        raise HTTPException(status_code=404, detail="Mundo não encontrado")
    for key, value in dados.dict().items():
        setattr(mundo, key, value)
    db.commit()
    db.refresh(mundo)
    return mundo

@router.delete("/{mundo_id}")
def deletar_mundo(mundo_id: int, db: Session = Depends(get_db)):
    mundo = db.query(MundoMagico).get(mundo_id)
    if not mundo:
        raise HTTPException(status_code=404, detail="Mundo não encontrado")
    db.delete(mundo)
    db.commit()
    return {"detail": "Mundo deletado com sucesso"}