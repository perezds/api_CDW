from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.transformacao import TransformacaoCreate, TransformacaoResponse
from crud import transformacao as crud_transformacao

router = APIRouter()

@router.post("/", response_model=TransformacaoResponse)
def criar_transformacao(transformacao: TransformacaoCreate, db: Session = Depends(get_db)):
    return crud_transformacao.criar_transformacao(db, transformacao)

@router.get("/", response_model=list[TransformacaoResponse])
def listar_transformacoes(db: Session = Depends(get_db)):
    return crud_transformacao.listar_transformacoes(db)
