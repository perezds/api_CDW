from fastapi import APIRouter
from api.v1.endpoints import winx, mundos
from routes import transformacao,episodio, poder,vilao

api_router = APIRouter()
api_router.include_router(winx.router)
api_router.include_router(mundos.router)  



api_router.include_router(transformacao.router, prefix="/transformacoes", tags=["Transformações"])
api_router.include_router(episodio.router, prefix="/episodios", tags=["Episódios"])
api_router.include_router(poder.router, prefix="/poderes", tags=["Poderes"])
api_router.include_router(vilao.router, prefix="/viloes", tags=["Vilões"])

