from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from core.database import Base, engine
=======
from api.v1 import api
from fastapi.middleware.cors import CORSMiddleware
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed

app = FastAPI(title="API Winx ✨")

app.include_router(api.api_router, prefix="/api/v1")

<<<<<<< HEAD
# Adicionando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Ou use ["*"] para permitir todos os domínios
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

app.include_router(api_router)
=======
app = FastAPI()


origins = [
    "http://localhost:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
