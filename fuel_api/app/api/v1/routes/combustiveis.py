from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.db.models.combustivel import Combustivel
from app.schemas.combustivel import CombustivelSchema
from typing import List

router = APIRouter()


@router.get("/combustiveis", response_model=List[CombustivelSchema])
async def get_combustiveis(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Combustivel))
    combustiveis = result.scalars().all()
    return combustiveis
