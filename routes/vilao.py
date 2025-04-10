from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.vilao import VilaoCreate, VilaoResponse
from crud import vilao as crud_vilao

router = APIRouter()

@router.post("/", response_model=VilaoResponse)
def criar_vilao(vilao: VilaoCreate, db: Session = Depends(get_db)):
    return crud_vilao.criar_vilao(db, vilao)

@router.get("/", response_model=list[VilaoResponse])
def listar_viloes(db: Session = Depends(get_db)):
    return crud_vilao.listar_viloes(db)
