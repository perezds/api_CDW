
from fastapi import FastAPI
from api.v1.api import api_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clube das Winx API")

app.include_router(api_router)
