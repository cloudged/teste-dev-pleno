from sqlalchemy.orm import Session
from app.models.order_model import Operacao
from app.schemas.order_schema import OrderCreate
from app.services.balance_service import update_balance
from app.services.fuel_price_service import get_purchase_price, get_sale_price


def create_order(db: Session, order_in: OrderCreate):
    ano = order_in.data.year
    mes = order_in.data.month
    tipo = order_in.tipo.lower()

    if tipo == "compra":
        ref = get_purchase_price(db, order_in.fuel_id, mes)
    elif tipo == "venda":
        ref = get_sale_price(db, order_in.fuel_id, mes)
    else:
        raise ValueError("Tipo inválido, deve ser 'compra' ou 'venda'")

    if not ref:
        raise ValueError(f"Nenhuma referência encontrada para {tipo} no mês {mes}")

    preco = float(ref.preco)
    tributo = float(ref.tributo)

    valor = preco * order_in.litros * (1 + tributo/100) * (1 + order_in.selic/100)

    db_operacao = Operacao(
        fuel_id=order_in.fuel_id,
        tipo=tipo,
        data=order_in.data,
        ref_id=ref.id,
        litros=order_in.litros,
        valor=round(valor, 2),
        selic=order_in.selic
    )

    db.add(db_operacao)
    db.commit()
    db.refresh(db_operacao)

    update_balance(db, tipo=order_in.tipo, ano=ano, valor=valor)

    return db_operacao
