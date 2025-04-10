from pydantic import BaseModel

class VilaoBase(BaseModel):
    nome: str
    descricao: str | None = None
    ameaca_nivel: str | None = None

class VilaoCreate(VilaoBase):
    pass

class VilaoResponse(VilaoBase):
    id: int

    class Config:
        orm_mode = True
