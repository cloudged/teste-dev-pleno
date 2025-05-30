from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.dependency import get_db
from app.models.fuel_model import Fuel
from app.schemas.fuel_schema import FuelResponse

from sqlalchemy import select

router = APIRouter(prefix="/fuel", tags=["fuel"])

@router.get("", response_model=List[FuelResponse])
def get_fuels(db: Session = Depends(get_db)):
    fuels = db.execute(select(Fuel)).scalars().all()
    return fuels
