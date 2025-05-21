from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clube das Winx API")

# Adicionando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Ou use ["*"] para permitir todos os domínios
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

app.include_router(api_router)
