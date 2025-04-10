from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.poder import PoderCreate, PoderResponse
from crud import poder as crud_poder

router = APIRouter()

@router.post("/", response_model=PoderResponse)
def criar_poder(poder: PoderCreate, db: Session = Depends(get_db)):
    return crud_poder.criar_poder(db, poder)

@router.get("/", response_model=list[PoderResponse])
def listar_poderes(db: Session = Depends(get_db)):
    return crud_poder.listar_poderes(db)
