from typing import List, Optional
from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository


class TaskService:

  def __init__(self, repository: TaskRepository):
    self.repository = repository

  def create_task(self, task_in: TaskCreate) -> TaskOut:
    # Aqui poderemos incluir regras de negócio futuras ou priorização por IA
    priority = task_in.priority or "média"
    return self.repository.create(task_in, priority=priority)

  def list_tasks(self) -> List[TaskOut]:
    return self.repository.list_all()

  def get_task(self, task_id: int) -> Optional[TaskOut]:
    return self.repository.get_by_id(task_id)

  def update_task(
      self, task_id: int, task_in: TaskUpdate
  ) -> Optional[TaskOut]:
    return self.repository.update(task_id, task_in)

  def delete_task(self, task_id: int) -> bool:
    return self.repository.delete(task_id)