from fastapi import FastAPI
from app.db.session import engine, Base



from app.api.v1.routes import combustiveis, preco_compra, preco_venda, operacoes

app = FastAPI()

# Cria as tabelas no banco (executar uma única vez ou no startup)
Base.metadata.create_all(bind=engine)

# Registrar rotas
app.include_router(combustiveis.router, prefix="/api/v1")
app.include_router(preco_compra.router, prefix="/api/v1", tags=["ref_compra"])
app.include_router(preco_venda.router, prefix="/api/v1", tags=["ref_venda"])
app.include_router(operacoes.router, prefix="/api/v1", tags=["operacoes"])


# Dependência para pegar a sessão DB nas rotas
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
