from typing import List, Optional
from app.repositories.task_repository import TaskRepository
from app.services.ai_service import AITaskService
from app.models.task_model import Task

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        priority = AITaskService.analyze_priority(title, description)
        return self.repository.create(title=title, description=description, priority=priority)

    def get_tasks(self, priority: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        return self.repository.list_all(priority=priority, completed=completed)

    def update_task(self, task_id: int, **update_data) -> Optional[Task]:
        return self.repository.update(task_id, **update_data)
