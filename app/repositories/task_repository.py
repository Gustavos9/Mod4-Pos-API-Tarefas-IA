from datetime import datetime
from typing import List, Optional
from app.models.task import TaskCreate, TaskOut, TaskUpdate


class TaskRepository:

  def __init__(self):
    self._tasks: List[TaskOut] = []
    self._id_counter = 1

  def create(self, task_in: TaskCreate, priority: str = "média") -> TaskOut:
    task = TaskOut(
        id=self._id_counter,
        title=task_in.title,
        description=task_in.description,
        completed=False,
        priority=priority,
        created_at=datetime.utcnow(),
    )
    self._tasks.append(task)
    self._id_counter += 1
    return task

  def list_all(self) -> List[TaskOut]:
    return self._tasks

  def get_by_id(self, task_id: int) -> Optional[TaskOut]:
    for task in self._tasks:
      if task.id == task_id:
        return task
    return None

  def update(self, task_id: int, task_in: TaskUpdate) -> Optional[TaskOut]:
    task = self.get_by_id(task_id)
    if not task:
      return None

    if task_in.title is not None:
      task.title = task_in.title
    if task_in.description is not None:
      task.description = task_in.description
    if task_in.completed is not None:
      task.completed = task_in.completed
    if task_in.priority is not None:
      task.priority = task_in.priority

    return task

  def delete(self, task_id: int) -> bool:
    task = self.get_by_id(task_id)
    if not task:
      return False
    self._tasks.remove(task)
    return True