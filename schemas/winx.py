from pydantic import BaseModel
from schemas.mundos import MundoMagicoResponse  

class WinxBase(BaseModel):
    nome: str
    poder_principal: str
    transformacao_favorita: str
    planeta_origem: str

class WinxCreate(WinxBase):
    mundo_id: int  

class WinxOut(WinxBase):
    id: int
    mundo: MundoMagicoResponse  

    class Config:
        orm_mode = True
