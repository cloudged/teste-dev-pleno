from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class RefVenda(Base):
    __tablename__ = "ref_venda"

    id = Column(Integer, primary_key=True, index=True)
    combustivel_id = Column(Integer, ForeignKey("combustivel.id"), nullable=False)  # corrigido para singular
    preco = Column(Float, nullable=False)
    mes = Column(Integer, nullable=False)

    combustivel = relationship("Combustivel", back_populates="vendas")
