from sqlalchemy import Column, Integer, String
from app.db.session import Base
from sqlalchemy.orm import relationship

class Combustivel(Base):
    __tablename__ = "combustivel"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)

    # Relacionamentos opcionais para compras e vendas
    compras = relationship("RefCompra", back_populates="combustivel")
    vendas = relationship("RefVenda", back_populates="combustivel")
