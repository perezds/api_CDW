from pydantic import BaseModel
from typing import List
from schemas.mundos import Mundo
from schemas.transformacao import TransformacaoResponse  

class WinxBase(BaseModel):
    nome: str
    poder_principal: str
    transformacao_favorita: str 
    planeta_origem: str

class WinxCreate(WinxBase):
    mundo_id: int  

class WinxOut(WinxBase):
    id: int
    mundo: Mundo 
    transformacoes: List[TransformacaoResponse] = []  

    class Config:
        orm_mode = True
