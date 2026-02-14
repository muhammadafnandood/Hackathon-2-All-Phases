import sys
from typing import Optional
from src.services.task_service import TaskService


class TodoCLI:
    """
    Command Line Interface for the Todo application.
    Handles user input and displays output.
    """
    
    def __init__(self):
        self.service = TaskService()
    
    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*40)
        print("         TODO APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("-"*40)
    
    def get_user_choice(self) -> str:
        """Get the user's menu choice."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            sys.exit(0)
    
    def add_task(self):
        """Handle adding a new task."""
        print("\n--- ADD TASK ---")
        title = input("Enter task title: ").strip()
        
        if not title:
            print("Task title cannot be empty.")
            return
        
        description = input("Enter task description (optional): ").strip()
        
        task = self.service.add_task(title, description)
        print(f"Task added successfully with ID: {task.id}")
    
    def view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- VIEW TASKS ---")
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        print(f"{'ID':<4} {'Title':<20} {'Description':<30} {'Status':<10}")
        print("-" * 70)
        
        for task in tasks:
            status = "✓ Completed" if task.completed else "○ Pending"
            desc = task.description[:27] + "..." if len(task.description) > 30 else task.description
            print(f"{task.id:<4} {task.title[:17]:<20} {desc:<30} {status:<10}")
    
    def update_task(self):
        """Handle updating a task."""
        print("\n--- UPDATE TASK ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        task = self.service.get_task_by_id(task_id)
        if not task:
            print(f"No task found with ID: {task_id}")
            return
        
        print(f"Current task: {task.title}")
        new_title = input(f"Enter new title (leave blank to keep '{task.title}'): ").strip()
        new_description = input(f"Enter new description (leave blank to keep current): ").strip()
        
        # Use None if user didn't provide new values to keep the original
        title = new_title if new_title else None
        description = new_description if new_description else None
        
        updated_task = self.service.update_task(task_id, title, description)
        if updated_task:
            print("Task updated successfully.")
        else:
            print("Failed to update task.")
    
    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- DELETE TASK ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        if self.service.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"No task found with ID: {task_id}")
    
    def mark_task_complete(self):
        """Handle marking a task as complete."""
        print("\n--- MARK TASK COMPLETE ---")
        try:
            task_id = int(input("Enter task ID to mark complete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        task = self.service.mark_task_complete(task_id)
        if task:
            print(f"Task with ID {task_id} marked as complete.")
        else:
            print(f"No task found with ID: {task_id}")
    
    def mark_task_incomplete(self):
        """Handle marking a task as incomplete."""
        print("\n--- MARK TASK INCOMPLETE ---")
        try:
            task_id = int(input("Enter task ID to mark incomplete: "))
        except ValueError:
            print("Invalid task ID. Please enter a number.")
            return
        
        task = self.service.mark_task_incomplete(task_id)
        if task:
            print(f"Task with ID {task_id} marked as incomplete.")
        else:
            print(f"No task found with ID: {task_id}")
    
    def run(self):
        """Run the CLI application."""
        print("Welcome to the Todo Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "7":
                print("Thank you for using the Todo Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            
            # Pause to allow user to see results before showing menu again
            input("\nPress Enter to continue...")