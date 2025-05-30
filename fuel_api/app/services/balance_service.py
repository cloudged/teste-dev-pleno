from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.balance_model import Balance


def update_balance(db: Session, tipo: str, ano: int, valor: float):
    balanco = db.query(Balance).filter(
        and_(Balance.tipo == tipo, Balance.ano == ano)
    ).first()

    if balanco:
        balanco.total += valor
    else:
        balanco = Balance(
            tipo=tipo,
            ano=ano,
            total=valor
        )
        db.add(balanco)

    db.commit()
    db.refresh(balanco)
    return balanco


def consult_balance_by_year(db: Session, ano: int):
    compras = db.query(Balance).filter(
        and_(Balance.ano == ano, Balance.tipo == "compra")
    ).first()

    vendas = db.query(Balance).filter(
        and_(Balance.ano == ano, Balance.tipo == "venda")
    ).first()

    total_compra = compras.total if compras else 0.0
    total_venda = vendas.total if vendas else 0.0
    diferenca = total_compra - total_venda

    return {
        "ano": ano,
        "total_compra": total_compra,
        "total_venda": total_venda,
        "diferenca": diferenca
    }
