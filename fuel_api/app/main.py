from fastapi import FastAPI
from app.db.session import engine, Base
from fastapi.middleware.cors import CORSMiddleware



from app.api.v1.routes import combustiveis, preco_compra, preco_venda, operacoes, balanco

app = FastAPI()

# Cria as tabelas no banco (executar uma única vez ou no startup)
Base.metadata.create_all(bind=engine)

# Registrar rotas
app.include_router(combustiveis.router, prefix="/api/v1", tags=["combustiveis"])
app.include_router(preco_compra.router, prefix="/api/v1", tags=["ref_compra"])
app.include_router(preco_venda.router, prefix="/api/v1", tags=["ref_venda"])
app.include_router(operacoes.router, prefix="/api/v1", tags=["operacoes"])
app.include_router(balanco.router, prefix="/api/v1", tags=["balanco"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (em desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os headers
)


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
