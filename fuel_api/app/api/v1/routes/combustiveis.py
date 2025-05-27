from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.dependency import get_db
from app.db.models.combustivel import Combustivel
from app.schemas.combustivel import CombustivelSchema

from sqlalchemy import select

router = APIRouter()

@router.get("/combustiveis", response_model=List[CombustivelSchema])
def get_combustiveis(db: Session = Depends(get_db)):
    combustiveis = db.execute(select(Combustivel)).scalars().all()
    return combustiveis
