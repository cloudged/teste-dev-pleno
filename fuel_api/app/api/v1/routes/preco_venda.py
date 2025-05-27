from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import Optional, List

from app.db.models.preco_venda import RefVenda
from app.schemas.preco_venda import PrecoVenda
from app.services.preco_venda import get_precos_venda

router = APIRouter()

@router.get("/ref_venda", response_model=List[PrecoVenda])
def listar_ref_venda(combustivel_id: Optional[int] = Query(None),
    mes: Optional[int] = Query(None), db: Session = Depends(get_db)):
    return get_precos_venda(db, combustivel_id=combustivel_id, mes=mes)
