from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.mundos import MundoMagico
from schemas.mundos import MundoResponse

router = APIRouter()

@router.get("/mundos/{mundo_id}", response_model=MundoResponse)
def get_mundo(mundo_id: int, db: Session):
    mundo = db.query(MundoMagico).filter(MundoMagico.id == mundo_id).first()
    if not mundo:
        raise HTTPException(status_code=404, detail="Mundo não encontrado")

    winx = [winx for winx in mundo.winx] 
    
    return MundoResponse(
        id=mundo.id,
        nome=mundo.nome,
        descricao=mundo.descricao,
        habitado_por=mundo.habitado_por,
        winx=winx  
    )
