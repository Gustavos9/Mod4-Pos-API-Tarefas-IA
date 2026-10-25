from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: Optional[str]
    priority: str
    completed: bool
    created_at: datetime
