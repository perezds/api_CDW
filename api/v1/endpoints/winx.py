from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.winx import WinxCreate, WinxOut
from models.winx import Winx

router = APIRouter()

@router.post("/", response_model=WinxOut)
def criar_personagem(winx: WinxCreate, db: Session = Depends(get_db)):
    db_winx = Winx(**winx.dict())
    db.add(db_winx)
    db.commit()
    db.refresh(db_winx)
    return db_winx

@router.get("/", response_model=list[WinxOut])
def listar_personagens(db: Session = Depends(get_db)):
    return db.query(Winx).all()
