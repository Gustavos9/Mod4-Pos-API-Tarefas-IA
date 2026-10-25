from typing import List, Optional
from datetime import datetime, timezone
from app.models.task_model import Task

class TaskRepository:
    def __init__(self):
        self._tasks: List[Task] = []
        self._counter: int = 1

    def create(self, title: str, description: Optional[str], priority: str) -> Task:
        task = Task(
            id=self._counter,
            title=title,
            description=description,
            priority=priority,
            completed=False,
            created_at=datetime.now(timezone.utc)
        )
        self._tasks.append(task)
        self._counter += 1
        return task

    def list_all(self, priority: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        filtered = self._tasks
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        return filtered

    def find_by_id(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task_id: int, **kwargs) -> Optional[Task]:
        task = self.find_by_id(task_id)
        if not task:
            return None
        for key, value in kwargs.items():
            if value is not None and hasattr(task, key):
                setattr(task, key, value)
        return task
