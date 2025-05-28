from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.balanco import consultar_balanco_por_ano
from app.schemas.balanco import BalancoConsultaResponse


router = APIRouter()


@router.get("/balanco", response_model=BalancoConsultaResponse)
def obter_balanco(
    ano: int = Query(..., description="Ano para consulta"),
    db: Session = Depends(get_db)
):
    resultado = consultar_balanco_por_ano(db, ano)
    return resultado
