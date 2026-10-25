from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task_schema import TaskCreateDTO, TaskUpdateDTO, TaskResponseDTO
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tarefas"])

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repository = TaskRepository(db)
    return TaskService(repository)

@router.post("/", response_model=TaskResponseDTO, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreateDTO, service: TaskService = Depends(get_task_service)):
    return service.create_task(title=task_data.title, description=task_data.description)

@router.get("/", response_model=List[TaskResponseDTO])
def list_tasks(
    priority: Optional[str] = Query(None, description="Filtrar por prioridade (alta, média, baixa)"),
    completed: Optional[bool] = Query(None, description="Filtrar por estado de conclusão"),
    service: TaskService = Depends(get_task_service)
):
    return service.get_tasks(priority=priority, completed=completed)

@router.patch("/{task_id}", response_model=TaskResponseDTO)
def update_task(task_id: int, task_data: TaskUpdateDTO, service: TaskService = Depends(get_task_service)):
    updated_task = service.update_task(task_id, **task_data.model_dump(exclude_unset=True))
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada."
        )
    return updated_task
