import select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from models.transformacao import Transformacao
from schemas.transformacao import TransformacaoCreate, TransformacaoResponse
from core.deps import get_session

router = APIRouter()

@router.post("/", response_model=TransformacaoResponse)
async def criar_transformacao(
    transformacao: TransformacaoCreate,
    db: AsyncSession = Depends(get_session)
):
    nova_transformacao = Transformacao(**transformacao.dict())
    db.add(nova_transformacao)
    await db.commit()
    await db.refresh(nova_transformacao)
    return nova_transformacao

@router.get("/", response_model=List[TransformacaoResponse])
async def listar_transformacoes(db: AsyncSession = Depends(get_session)):
    result = await db.execute(
        select(Transformacao)
    )
    return result.scalars().all()

@router.get("/{transformacao_id}", response_model=TransformacaoResponse)
async def get_transformacao(transformacao_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.get(Transformacao, transformacao_id)
    if not result:
        raise HTTPException(status_code=404, detail="Transformação não encontrada")
    return result
