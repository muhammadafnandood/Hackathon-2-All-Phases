# Task CRUD Feature Specification

## Overview

The Task CRUD feature allows users to perform basic operations on tasks: Create, Read, Update, and Delete.

## Functional Requirements

### 1. Add Task
- User can add a new task with a title
- User can optionally add a description
- System assigns a unique ID to the task
- Task is initially marked as incomplete
- Task records creation and update timestamps

### 2. View Tasks
- User can view all tasks
- Display includes ID, title, description, and completion status
- Tasks are displayed in a tabular format

### 3. Update Task
- User can update the title of an existing task
- User can update the description of an existing task
- System updates the task's modification timestamp
- Operation fails if the task ID does not exist

### 4. Delete Task
- User can delete a task by its ID
- Operation fails if the task ID does not exist
- Once deleted, the task is permanently removed

## Non-functional Requirements

- Operations should complete within 1 second
- In-memory storage is sufficient
- Data is not persisted between application runs
- User-friendly command-line interface

## Error Handling

- Invalid task IDs should result in appropriate error messages
- Empty titles should be rejected when adding tasks
- Missing tasks should be handled gracefully when updating/deleting