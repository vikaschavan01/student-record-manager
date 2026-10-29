
# Student Record Manager

A Python-based console application for managing student records using object-oriented programming, modular code, input validation, and JSON file storage.

## Features

- Add new student records
- View all student records
- Search students by name
- Update student information
- Delete student records
- Calculate average and highest marks
- Display class statistics
- Validate names and marks
- Save and load records using JSON
- Unit testing with Python's unittest framework

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- pathlib
- unittest
- Git and GitHub

## Project Structure

```text
student_record_manager/
├── main.py
├── student.py
├── storage.py
├── tests/
│   └── test_student.py
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.
2. Open the project folder in your terminal.
3. Create and activate a virtual environment.
4. Run the application.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python main.py
```

## Run Tests

```powershell
python -m unittest discover -s tests -v
```

## Learning Objectives

This project demonstrates Python classes, functions, modular programming, exception handling, data persistence, and automated testing.
