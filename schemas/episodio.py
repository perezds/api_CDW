from pydantic import BaseModel

class EpisodioBase(BaseModel):
    numero: int
    temporada: int
    titulo: str
    sinopse: str | None = None

class EpisodioCreate(EpisodioBase):
    pass

class EpisodioResponse(EpisodioBase):
    id: int

    class Config:
        orm_mode = True
