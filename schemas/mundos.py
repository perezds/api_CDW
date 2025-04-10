from pydantic import BaseModel

class MundoBase(BaseModel):
    nome: str
    descricao: str
    habitado_por: str

class MundoCreate(MundoBase):
    pass

class Mundo(MundoBase):
    id: int

    class Config:
        orm_mode = True
