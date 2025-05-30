from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.balance_service import consult_balance_by_year
from app.schemas.balance_schema import BalanceResponse


router = APIRouter(prefix="/balance", tags=["balance"])


@router.get("", response_model=BalanceResponse)
def get_balance(
    ano: int = Query(..., description="Ano para consulta"),
    db: Session = Depends(get_db)
):
    resultado = consult_balance_by_year(db, ano)
    return resultado
