from pydantic import BaseModel

class PoderBase(BaseModel):
    nome: str
    descricao: str | None = None

class PoderCreate(PoderBase):
    pass

class PoderResponse(PoderBase):
    id: int

    class Config:
        orm_mode = True
