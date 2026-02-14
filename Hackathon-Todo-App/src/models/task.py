from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """
    Represents a task in the todo application.
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None
    updated_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False
        self.updated_at = datetime.now()

    def update(self, title: str = None, description: str = None):
        """Update the task details."""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()