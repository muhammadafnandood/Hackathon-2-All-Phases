from typing import List, Optional
from src.models.task import Task


class TaskService:
    """
    Service layer for managing tasks.
    Implements the business logic for task operations.
    """
    
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task to the list."""
        task = Task(
            id=self._next_id,
            title=title,
            description=description
        )
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks."""
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> Optional[Task]:
        """Update a task's details."""
        task = self.get_task_by_id(task_id)
        if task:
            task.update(title, description)
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False
    
    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """Mark a task as complete."""
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_complete()
        return task
    
    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        """Mark a task as incomplete."""
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_incomplete()
        return task