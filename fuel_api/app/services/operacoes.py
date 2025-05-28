from sqlalchemy.orm import Session
from app.db.models.operacoes import Operacao
from app.schemas.operacoes import OperacaoCreate
from datetime import date
from app.services.balanco import atualizar_balanco

from app.services import preco_compra, preco_venda


def criar_operacao(db: Session, operacao_in: OperacaoCreate):
    ano = operacao_in.data.year
    mes = operacao_in.data.month
    tipo = operacao_in.tipo.lower()

    # Busca referência no serviço correto
    if tipo == "compra":
        ref = preco_compra.buscar_referencia(db, operacao_in.combustivel_id, mes)
    elif tipo == "venda":
        ref = preco_venda.buscar_referencia(db, operacao_in.combustivel_id, mes)
    else:
        raise ValueError("Tipo inválido, deve ser 'compra' ou 'venda'")

    if not ref:
        raise ValueError(f"Nenhuma referência encontrada para {tipo} no mês {mes}")

    preco = float(ref.preco)
    tributo = float(ref.tributo)

    valor = preco * float(operacao_in.litros) * tributo * float(operacao_in.selic)

    db_operacao = Operacao(
        combustivel_id=operacao_in.combustivel_id,
        tipo=tipo,
        data=operacao_in.data,
        ref_id=ref.id,
        litros=operacao_in.litros,
        valor=round(valor, 2),
        selic=operacao_in.selic
    )

    db.add(db_operacao)
    db.commit()
    db.refresh(db_operacao)

    atualizar_balanco(db, tipo=operacao_in.tipo, ano=ano, valor=valor)

    return db_operacao
