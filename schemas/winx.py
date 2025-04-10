from pydantic import BaseModel

class WinxBase(BaseModel):
    nome: str
    poder: str
    planeta_origem: str
    transformacao_favorita: str

class WinxCreate(WinxBase):
    pass

class WinxOut(WinxBase):
    id: int

    class Config:
        orm_mode = True
