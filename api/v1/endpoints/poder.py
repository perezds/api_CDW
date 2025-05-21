from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_poderes():
    return {"msg": "Poderes em construção!"}
