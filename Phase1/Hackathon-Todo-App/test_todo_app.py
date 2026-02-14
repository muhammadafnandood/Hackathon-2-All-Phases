import unittest
from src.models.task import Task
from src.services.task_service import TaskService


class TestTaskModel(unittest.TestCase):
    """Test cases for the Task model."""
    
    def test_create_task(self):
        """Test creating a new task."""
        task = Task(id=1, title="Test Task", description="Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
    
    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task(id=1, title="Test Task")
        self.assertFalse(task.completed)
        task.mark_complete()
        self.assertTrue(task.completed)
    
    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task(id=1, title="Test Task")
        task.mark_complete()  # First mark as complete
        self.assertTrue(task.completed)
        task.mark_incomplete()
        self.assertFalse(task.completed)
    
    def test_update_task(self):
        """Test updating task details."""
        task = Task(id=1, title="Old Title", description="Old Description")
        task.update(title="New Title", description="New Description")
        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "New Description")


class TestTaskService(unittest.TestCase):
    """Test cases for the TaskService."""
    
    def setUp(self):
        """Set up a fresh service for each test."""
        self.service = TaskService()
    
    def test_add_task(self):
        """Test adding a task."""
        task = self.service.add_task("Test Task", "Test Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        self.service.add_task("Task 1", "Description 1")
        self.service.add_task("Task 2", "Description 2")
        
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")
    
    def test_get_task_by_id(self):
        """Test retrieving a task by ID."""
        added_task = self.service.add_task("Test Task", "Test Description")
        retrieved_task = self.service.get_task_by_id(added_task.id)
        
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, added_task.id)
        self.assertEqual(retrieved_task.title, added_task.title)
    
    def test_update_task(self):
        """Test updating a task."""
        task = self.service.add_task("Old Title", "Old Description")
        updated_task = self.service.update_task(task.id, "New Title", "New Description")
        
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
    
    def test_delete_task(self):
        """Test deleting a task."""
        task = self.service.add_task("Test Task", "Test Description")
        initial_count = len(self.service.get_all_tasks())
        
        result = self.service.delete_task(task.id)
        
        self.assertTrue(result)
        self.assertEqual(len(self.service.get_all_tasks()), initial_count - 1)
        
        # Verify the task is gone
        deleted_task = self.service.get_task_by_id(task.id)
        self.assertIsNone(deleted_task)
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.service.add_task("Test Task", "Test Description")
        self.assertFalse(task.completed)
        
        marked_task = self.service.mark_task_complete(task.id)
        self.assertTrue(marked_task.completed)
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.service.add_task("Test Task", "Test Description")
        task.mark_complete()  # First mark as complete
        self.assertTrue(task.completed)
        
        marked_task = self.service.mark_task_incomplete(task.id)
        self.assertFalse(marked_task.completed)


if __name__ == '__main__':
    unittest.main()