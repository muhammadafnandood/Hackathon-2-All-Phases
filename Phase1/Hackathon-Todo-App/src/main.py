#!/usr/bin/env python3
"""
Main entry point for the Todo Application.
"""

from src.cli.todo_cli import TodoCLI


def main():
    """Main function to run the application."""
    app = TodoCLI()
    app.run()


if __name__ == "__main__":
    main()