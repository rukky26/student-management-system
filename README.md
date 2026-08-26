# Student Management System

A command-line Student Management System built with Python. The application allows users to add, view, search, update, and delete student records while storing data locally in JSON format.

## Features

* Add new student records
* View all registered students
* Search for a student using their matriculation number
* Update student information
* Delete student records
* Validate required fields
* Validate student level
* Prevent duplicate matriculation numbers
* Save student records using JSON
* Load previously saved records when the application starts

## Technologies Used

* **Python 3**
* **JSON**
* **Git**
* **GitHub**

## Project Structure

```text
student-management-system/
│
├── .gitignore
├── LICENSE
├── README.md
├── student_management.py
└── students.json
```

> `students.json` is excluded from Git tracking to prevent student data from being uploaded to the public repository.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rukky26/student-management-system.git
```

### 2. Navigate into the project directory

```bash
cd student-management-system
```

### 3. Run the application

```bash
python student_management.py
```

## How It Works

When the application starts, it loads existing student records from `students.json`.

The main menu provides six options:

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

Student records contain:

* Name
* Matriculation number
* Department
* Level

## Data Storage

Student records are stored locally in a JSON file.

Example structure:

```json
[
    {
        "name": "John Doe",
        "matric_number": "234",
        "department": "Computer Science",
        "level": "300"
    }
]
```

The data file is intentionally excluded from Git using `.gitignore` so that personal student information is not accidentally published.

## Future Improvements

Planned improvements include:

* Add a graphical user interface
* Add stronger input validation
* Add student sorting and filtering
* Add automated tests
* Replace JSON storage with a database
* Add user authentication
* Improve error handling
* Add role-based access for administrators

## Learning Objectives

This project was created to practice:

* Python programming
* Functions
* Dictionaries and lists
* Loops and conditional statements
* File handling
* JSON data storage
* Input validation
* CRUD operations
* Git version control
* GitHub project management

## Author

**Rukky Ororho**

Computer Science Student | Aspiring Cybersecurity Professional
