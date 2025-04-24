from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_transformacoes():
    return {"msg": "Transformações em breve"}
