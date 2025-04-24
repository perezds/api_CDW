from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.poder import PoderCreate, PoderResponse
from crud import poder as crud_poder
from models.poder import Poder

router = APIRouter()

@router.post("/", response_model=PoderResponse)
def criar_poder(poder: PoderCreate, db: Session = Depends(get_db)):
    db_poder = poder(**poder.dict())
    db.add(db_poder)
    db.commit()
    db.refresh(db_poder)
    return db_poder

@router.get("/", response_model=List[PoderResponse])
def listar_poders(db: Session = Depends(get_db)):
    return db.query(Poder).all()

@router.get("/{poder_id}", response_model=PoderResponse)
def obter_poder(poder_id: int, db: Session = Depends(get_db)):
    poder = db.query(Poder).get(poder_id)
    if not poder:
        raise HTTPException(status_code=404, detail="Poder não encontrado")
    return poder

@router.put("/{poder_id}", response_model=PoderResponse)
def atualizar_poder(poder_id: int, dados:PoderCreate, db: Session = Depends(get_db)):
    poder = db.query(Poder).get(poder_id)
    if not poder:
        raise HTTPException(status_code=404, detail="Poder não encontrado")
    for key, value in dados.dict().items():
        setattr(poder, key, value)
    db.commit()
    db.refresh(poder)
    return poder

@router.delete("/{poder_id}")
def deletar_poder(poder_id: int, db: Session = Depends(get_db)):
    poder = db.query(Poder).get(poder_id)
    if not poder:
        raise HTTPException(status_code=404, detail="Poder não encontrado")
    db.delete(poder)
    db.commit()
    return {"detail": "Poder deletado com sucesso"}
