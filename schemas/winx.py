from pydantic import BaseModel
from typing import List
<<<<<<< HEAD
from schemas.mundos import Mundo
from schemas.transformacao import TransformacaoResponse  
=======

from schemas.poder import PoderResponse
from schemas.episodio import EpisodioResponse 
from schemas.transformacao import TransformacaoResponse
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed

class WinxBase(BaseModel):
    nome: str
    poder_principal: str
    transformacao_favorita: str 
    planeta_origem: str

class WinxCreate(WinxBase):
    mundo_id: int 

class WinxOut(WinxBase):
    id: int
<<<<<<< HEAD
    mundo: Mundo 
    transformacoes: List[TransformacaoResponse] = []  
=======
    mundo: "MundoResponse"  
    fadas: List[str]
    poderes: List[PoderResponse]
    episodios: List[EpisodioResponse]
    transformacoes: List[TransformacaoResponse]
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed

    class Config:
        orm_mode = True

# IMPORT NO FINAL pra evitar o loop do capeta
from schemas.mundos import MundoResponse
