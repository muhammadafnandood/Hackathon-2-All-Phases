# Hackathon Todo App

A spec-driven console todo application built in Python with clean architecture.

## Features

- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as complete/incomplete
- In-memory storage
- CLI menu interface

## Architecture

The application follows clean architecture principles with the following layers:

- **Models**: Define the data structures (Task model)
- **Services**: Handle business logic (TaskService)
- **CLI**: Handle user interface and interaction (TodoCLI)

## Setup

1. Clone the repository
2. Install dependencies: `pip install -e .` or `poetry install`
3. Run the application: `python -m src.main` or `poetry run todo`

## Usage

The application provides a menu-driven interface:

1. Add Task - Create a new task with title and description
2. View Tasks - See all tasks with their status
3. Update Task - Modify existing task details
4. Delete Task - Remove a task
5. Mark Task Complete - Mark a task as completed
6. Mark Task Incomplete - Mark a task as pending
7. Exit - Quit the application

## Project Structure

```
src/
├── main.py          # Entry point
├── models/
│   └── task.py      # Task data model
├── services/
│   └── task_service.py  # Business logic
└── cli/
    └── todo_cli.py  # Command line interface
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request