from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.winx import Fada 
from schemas.winx import FadaResponse

router = APIRouter(prefix="/fada", tags=["Fadas"])

@router.get("/{nome}", response_model=FadaResponse)
def buscar_fada_por_nome(nome: str, db: Session = Depends(get_db)):
    fada = db.query(Fada).filter(Fada.nome.ilike(nome)).first()
    if not fada:
        raise HTTPException(status_code=404, detail="Fada não encontrada!")
    return fada
