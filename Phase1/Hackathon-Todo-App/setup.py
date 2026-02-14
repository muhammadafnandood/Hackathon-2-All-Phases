from setuptools import setup, find_packages

setup(
    name="todo-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'todo-app=src.main:main',
        ],
    },
    author="Todo App Developer",
    description="A spec-driven console todo application in Python",
    python_requires='>=3.6',
)