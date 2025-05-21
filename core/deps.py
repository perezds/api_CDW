<<<<<<< HEAD
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import SessionLocal

async def get_session() -> Generator:
    session: AsyncSession = SessionLocal()
    try:
        yield session
    finally:
        await session.close()
=======
from .database import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
>>>>>>> d152c127a6bb0676f6709e6d1d9cd40e9bcb3eed
