from fastapi import FastAPI
from api.v1 import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Winx ✨")

app.include_router(api.api_router, prefix="/api/v1")

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