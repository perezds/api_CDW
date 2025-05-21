from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.vilao import Vilao
from schemas.vilao import VilaoCreate, VilaoResponse
from crud import vilao as crud_vilao
from typing import List

router = APIRouter()

@router.post("/", response_model=VilaoResponse)
def criar_vilao(vilao: VilaoCreate, db: Session = Depends(get_db)):
    db_vilao = vilao(**vilao.dict())
    db.add(db_vilao)
    db.commit()
    db.refresh(db_vilao)
    return db_vilao

@router.get("/", response_model=List[VilaoResponse])
def listar_vilaos(db: Session = Depends(get_db)):
    return db.query(Vilao).all()

@router.get("/{vilao_id}", response_model=VilaoResponse)
def obter_vilao(vilao_id: int, db: Session = Depends(get_db)):
    vilao = db.query(Vilao).get(vilao_id)
    if not vilao:
        raise HTTPException(status_code=404, detail="vilao não encontrado")
    return vilao

@router.put("/{vilao_id}", response_model=VilaoResponse)
def atualizar_vilao(vilao_id: int, dados:VilaoCreate, db: Session = Depends(get_db)):
    vilao = db.query(Vilao).get(vilao_id)
    if not vilao:
        raise HTTPException(status_code=404, detail="vilao não encontrado")
    for key, value in dados.dict().items():
        setattr(vilao, key, value)
    db.commit()
    db.refresh(vilao)
    return vilao

@router.delete("/{vilao_id}")
def deletar_vilao(vilao_id: int, db: Session = Depends(get_db)):
    vilao = db.query(Vilao).get(vilao_id)
    if not vilao:
        raise HTTPException(status_code=404, detail="vilao não encontrado")
    db.delete(vilao)
    db.commit()
    return {"detail": "vilao deletado com sucesso"}
