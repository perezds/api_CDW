from pydantic import BaseModel
from typing import List

from schemas.poder import PoderResponse
from schemas.episodio import EpisodioResponse 
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
    mundo: "MundoResponse"  
    fadas: List[str]
    poderes: List[PoderResponse]
    episodios: List[EpisodioResponse]
    transformacoes: List[TransformacaoResponse]

    class Config:
        orm_mode = True

# IMPORT NO FINAL pra evitar o loop do capeta
from schemas.mundos import MundoResponse
