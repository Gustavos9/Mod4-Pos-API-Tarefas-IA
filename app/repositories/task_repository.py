from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, description: Optional[str], priority: str) -> Task:
        task = Task(
            title=title,
            description=description,
            priority=priority,
            completed=False,
            created_at=datetime.now(timezone.utc)
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def list_all(self, priority: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        query = self.db.query(Task)
        if priority:
            query = query.filter(Task.priority == priority)
        if completed is not None:
            query = query.filter(Task.completed == completed)
        return query.all()

    def find_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update(self, task_id: int, **kwargs) -> Optional[Task]:
        task = self.find_by_id(task_id)
        if not task:
            return None
        for key, value in kwargs.items():
            if value is not None and hasattr(task, key):
                setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task
