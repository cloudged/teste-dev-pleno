from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.db.models.balanco import Balanco


def atualizar_balanco(db: Session, tipo: str, ano: int, valor: float):
    balanco = db.query(Balanco).filter(
        and_(Balanco.tipo == tipo, Balanco.ano == ano)
    ).first()

    if balanco:
        balanco.total += valor
    else:
        balanco = Balanco(
            tipo=tipo,
            ano=ano,
            total=valor
        )
        db.add(balanco)

    db.commit()
    db.refresh(balanco)
    return balanco


def consultar_balanco_por_ano(db: Session, ano: int):
    compras = db.query(Balanco).filter(
        and_(Balanco.ano == ano, Balanco.tipo == "compra")
    ).first()

    vendas = db.query(Balanco).filter(
        and_(Balanco.ano == ano, Balanco.tipo == "venda")
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
