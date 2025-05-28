from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.operacoes import OperacaoResponse, OperacaoCreate
from app.services.operacoes import criar_operacao

router = APIRouter()


@router.post("/operacoes", response_model=OperacaoResponse)
def criar_operacao_endpoint(
    operacao_in: OperacaoCreate,
    db: Session = Depends(get_db)
):
    try:
        operacao = criar_operacao(db, operacao_in)
        return operacao
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
