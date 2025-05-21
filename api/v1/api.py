from fastapi import APIRouter
<<<<<<< HEAD
from api.v1.endpoints import winx, mundos
from routes import transformacao, episodio, poder, vilao

api_router = APIRouter()

api_router.include_router(winx.router, prefix="/winx", tags=["Winx"])
api_router.include_router(mundos.router, prefix="/mundos", tags=["Mundos"])
api_router.include_router(transformacao.router, prefix="/transformacoes", tags=["Transformações"])
api_router.include_router(episodio.router, prefix="/episodios", tags=["Episódios"])
api_router.include_router(poder.router, prefix="/poderes", tags=["Poderes"])
api_router.include_router(vilao.router, prefix="/viloes", tags=["Vilões"])
=======
from .endpoints import vilao, transformacao, mundos, poder, episodio, winx

api_router = APIRouter()
api_router.include_router(vilao.router, prefix="/viloes", tags=["Vilões"])
api_router.include_router(transformacao.router, prefix="/transformacoes", tags=["Transformações"])
api_router.include_router(mundos.router, prefix="/mundos", tags=["Mundos Mágicos"])
api_router.include_router(poder.router, prefix="/poderes", tags=["Poderes"])
api_router.include_router(episodio.router, prefix="/episodios", tags=["Episódios"])
api_router.include_router(winx.router, prefix="/winx", tags=["Fadas"])
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
