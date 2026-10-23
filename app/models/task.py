from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
  title: str = Field(..., min_length=1, description="Título da tarefa")
  description: Optional[str] = Field(None, description="Descrição detalhada")
  priority: str = Field(
      "média", description="Prioridade: baixa, média ou alta"
  )


class TaskUpdate(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None
  completed: Optional[bool] = None
  priority: Optional[str] = None


class TaskOut(BaseModel):
  id: int
  title: str
  description: Optional[str] = None
  completed: bool
  priority: str
  created_at: datetime