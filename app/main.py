from fastapi import FastAPI
from datetime import datetime
from app.database import engine, Base
from app.routers import task_router

# Cria as tabelas na base de dados se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gerenciamento de Tarefas com IA",
    version="5.0.0",
    description="API robusta em FastAPI com priorização automática por IA e persistência SQLAlchemy."
)

app.include_router(task_router.router)

@app.get("/health", tags=["Sistema"])
def health_check():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}
