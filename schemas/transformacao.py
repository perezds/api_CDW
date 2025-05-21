from pydantic import BaseModel

class TransformacaoBase(BaseModel):
    nome: str
    descricao: str | None = None
    nivel_magico: str | None = None
    winx_id: int

class TransformacaoCreate(TransformacaoBase):
    pass

class TransformacaoResponse(TransformacaoBase):
    id: int

    class Config:
        orm_mode = True
