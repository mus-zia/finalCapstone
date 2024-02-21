# Task Manager Program README

## Project Name
Task Manager Program

## Description
The Task Manager Program is a simple, yet powerful task management system. It allows users to register, add, view, and manage tasks. It also provides the functionality to generate and display reports on tasks and users. The program is designed to be modular, with the task management functions moved to a separate file to avoid congestion in the main file.

The importance of this project lies in its ability to help individuals and teams manage their tasks more efficiently. It provides a structured way to track tasks, set due dates, and monitor progress. Furthermore, it offers a detailed report on task completion and user contribution, which can be beneficial for project management and team coordination.

## Table of Contents
- [Project Name](#project-name)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation
To install and run this project locally, follow these steps:

1. Clone or download the repository to your local machine.
2. Ensure you have Python  3 installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).
3. Open a terminal or command prompt and navigate to the directory where you cloned or downloaded the repository.
4. Run the main file, `task_manager.py`, using the command `python task_manager.py`.

Please note that the program looks for the text files `tasks.txt` and `user.txt` in the same directory as the main file. Make sure these files exist or create them if they don't.

## Usage
Once the program is running, you will be presented with a menu to select from various options. Here's a brief overview of what each option does:

- `r` - Register a new user.
- `a` - Add a new task.
- `va` - View all tasks.
- `vm` - View tasks assigned to the current user.
- `mt` - Manage tasks (mark as complete or edit).
- `gr` - Generate reports.
- `ds` - Display statistics (only available to the admin).
- `e` - Exit the program.

To use the program, select an option from the menu and follow the prompts. For example, to add a task, select `a`, then input the required details for the task.

Please note that to view statistics, you must be logged in as the admin user. The default admin credentials are `username: admin` and `password: password`.

## Credits
This project was created by a single developer. However, it uses libraries and modules from the Python Standard Library, such as `os`, `datetime`, and `date`.
