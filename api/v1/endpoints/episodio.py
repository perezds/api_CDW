from fastapi import APIRouter

router = APIRouter()

@router.get("/episodios")
def listar_episodios():
    return {"msg": "Lista de episódios em construção 🚧"}
