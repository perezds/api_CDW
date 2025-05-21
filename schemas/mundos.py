from pydantic import BaseModel
from typing import List

class MundoBase(BaseModel):
    nome: str
    descricao: str

class MundoCreate(MundoBase):
    pass

class MundoResponse(MundoBase):
    id: int
    winx: List["WinxOut"]  

    class Config:
        orm_mode = True

# IMPORT NO FINAL
from schemas.winx import WinxOut
