from typing import List
from fastapi import APIRouter, HTTPException, status
from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tarefas"])

# Instância partilhada do repositório e serviço (em memória)
repository = TaskRepository()
service = TaskService(repository)


@router.post(
    "/", response_model=TaskOut, status_code=status.HTTP_201_CREATED
)
def create_task(task_in: TaskCreate):
  return service.create_task(task_in)


@router.get("/", response_model=List[TaskOut])
def list_tasks():
  return service.list_tasks()


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
  task = service.get_task(task_id)
  if not task:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
    )
  return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_in: TaskUpdate):
  task = service.update_task(task_id, task_in)
  if not task:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
    )
  return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
  success = service.delete_task(task_id)
  if not success:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
    )
  return None