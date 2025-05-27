from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.models.preco_venda import RefVenda
from app.schemas.preco_venda import PrecoVenda


def get_precos_venda(
    db: Session, combustivel_id: Optional[int] = None, mes: Optional[int] = None
) -> List[RefVenda]:
    query = db.query(RefVenda)
    if combustivel_id:
        query = query.filter(RefVenda.combustivel_id == combustivel_id)
    if mes:
        query = query.filter(RefVenda.mes == mes)
    return query.all()
