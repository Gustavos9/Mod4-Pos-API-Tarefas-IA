from datetime import datetime
from fastapi import FastAPI
from app.routers import task_router

app = FastAPI(
    title="Micro-API de Tarefas",
    description="MVP de gestão de tarefas com priorização assistida por IA",
    version="1.0.0",
)

# Incluir as rotas de tarefas
app.include_router(task_router.router)


@app.get("/health")
def health_check():
  return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}