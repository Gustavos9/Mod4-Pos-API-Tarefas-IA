from datetime import datetime
from fastapi import FastAPI

app = FastAPI(
    title="Micro-API de Tarefas",
    description="MVP de gestão de tarefas com priorização assistida por IA",
    version="1.0.0",
)


@app.get("/health")
def health_check():
  return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}