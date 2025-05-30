from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.db.session import Base


class Operacao(Base):
    __tablename__ = "fuel_order"

    id = Column(Integer, primary_key=True, index=True)
    fuel_id = Column(Integer, ForeignKey("fuel.id"), nullable=False)
    tipo = Column(String(10), nullable=False)
    data = Column(Date, nullable=False)
    ref_id = Column(Integer, nullable=False)
    litros = Column(Numeric(10, 2), nullable=False)
    valor = Column(Numeric(15, 2), nullable=False)
    selic = Column(Numeric(5, 2), nullable=False)

    fuel = relationship("Fuel")

    __table_args__ = (
        CheckConstraint("tipo IN ('compra', 'venda')", name="check_tipo_operacao"),
    )
