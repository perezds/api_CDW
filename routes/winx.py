from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.winx import Fada
from schemas.winx import FadaCreate, FadaResponse
from typing import List

router = APIRouter(prefix="/fada", tags=["Fadas"])

@router.post("/", response_model=FadaResponse)
def criar_fada(fada: FadaCreate, db: Session = Depends(get_db)):
    nova_fada = Fada(**fada.dict())
    db.add(nova_fada)
    db.commit()
    db.refresh(nova_fada)
    return nova_fada

@router.get("/", response_model=List[FadaResponse])
def listar_fadas(db: Session = Depends(get_db)):
    return db.query(Fada).all()

@router.get("/{nome}", response_model=FadaResponse)
def buscar_fada_por_nome(nome: str, db: Session = Depends(get_db)):
    fada = db.query(Fada).filter(Fada.nome.ilike(nome)).first()
    if not fada:
        raise HTTPException(status_code=404, detail="Fada não encontrada!")
    return fada

@router.put("/{id}", response_model=FadaResponse)
def atualizar_fada(id: int, dados: FadaCreate, db: Session = Depends(get_db)):
    fada = db.query(Fada).get(id)
    if not fada:
        raise HTTPException(status_code=404, detail="Fada não encontrada!")
    for key, value in dados.dict().items():
        setattr(fada, key, value)
    db.commit()
    db.refresh(fada)
    return fada

@router.delete("/{id}")
def deletar_fada(id: int, db: Session = Depends(get_db)):
    fada = db.query(Fada).get(id)
    if not fada:
        raise HTTPException(status_code=404, detail="Fada não encontrada!")
    db.delete(fada)
    db.commit()
    return {"detail": "Fada deletada com sucesso!"}
