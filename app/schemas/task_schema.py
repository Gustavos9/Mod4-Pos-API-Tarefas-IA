from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class TaskUpdateDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[str] = Field(None, pattern="^(alta|média|baixa)$")
    completed: Optional[bool] = None

class TaskResponseDTO(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
