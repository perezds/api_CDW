from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.transformacao import Transformacao
from schemas.transformacao import TransformacaoCreate, TransformacaoResponse
from crud import transformacao as crud_transformacao

router = APIRouter()

@router.post("/", response_model=TransformacaoResponse)
def criar_transformacao(transformacao: TransformacaoCreate, db: Session = Depends(get_db)):
    db_transformacao = transformacao(**transformacao.dict())
    db.add(db_transformacao)
    db.commit()
    db.refresh(db_transformacao)
    return db_transformacao

@router.get("/", response_model=List[TransformacaoResponse])
def listar_transformacaos(db: Session = Depends(get_db)):
    return db.query(Transformacao).all()

@router.get("/{transformacao_id}", response_model=TransformacaoResponse)
def obter_transformacao(transformacao_id: int, db: Session = Depends(get_db)):
    transformacao = db.query(Transformacao).get(transformacao_id)
    if not transformacao:
        raise HTTPException(status_code=404, detail="transformacao não encontrado")
    return transformacao

@router.put("/{transformacao_id}", response_model=TransformacaoResponse)
def atualizar_transformacao(transformacao_id: int, dados:TransformacaoCreate, db: Session = Depends(get_db)):
    transformacao = db.query(Transformacao).get(transformacao_id)
    if not transformacao:
        raise HTTPException(status_code=404, detail="transformacao não encontrado")
    for key, value in dados.dict().items():
        setattr(transformacao, key, value)
    db.commit()
    db.refresh(transformacao)
    return transformacao

@router.delete("/{transformacao_id}")
def deletar_transformacao(transformacao_id: int, db: Session = Depends(get_db)):
    transformacao = db.query(Transformacao).get(transformacao_id)
    if not transformacao:
        raise HTTPException(status_code=404, detail="transformacao não encontrado")
    db.delete(transformacao)
    db.commit()
    return {"detail": "transformacao deletado com sucesso"}
