"""
Student Management System

A command-line application for managing student records.
Student data is stored locally in a JSON file.
"""

import json


FILE_NAME = "students.json"


def load_students():
    """Load student records from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Student data file is corrupted.")
        return []


students = load_students()


def get_non_empty_input(prompt):
    """Request input from the user until a non-empty value is provided."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")


def get_level():
    """Request and validate a university student level."""
    while True:
        level = input("Enter level: ").strip()

        if level.isdigit() and int(level) > 0:
            return level

        print("Please enter a valid level, such as 100, 200, 300, or 400.")


def save_students():
    """Save student records to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error: Unable to save student data.")


def add_student():
    """Add a new student to the system."""
    print("\n--- Add Student ---")

    name = get_non_empty_input("Enter student name: ").title()
    matric_number = get_non_empty_input("Enter matric number: ").upper()
    department = get_non_empty_input("Enter department: ").title()
    level = get_level()

    for student in students:
        if student["matric_number"] == matric_number:
            print("A student with this matric number already exists.")
            return

    student = {
        "name": name,
        "matric_number": matric_number,
        "department": department,
        "level": level
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    """Display all registered students."""
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Matric Number: {student['matric_number']}")
        print(f"Department: {student['department']}")
        print(f"Level: {student['level']}")
        print("-" * 30)


def search_student():
    """Search for a student using their matriculation number."""
    print("\n--- Search Student ---")

    matric_number = get_non_empty_input("Enter matric number: ").upper()

    for student in students:
        if student["matric_number"] == matric_number:
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Matric Number: {student['matric_number']}")
            print(f"Department: {student['department']}")
            print(f"Level: {student['level']}")
            return

    print("\nStudent not found.")


def update_student():
    """Update an existing student's information."""
    print("\n--- Update Student ---")

    matric_number = get_non_empty_input(
        "Enter matric number of student to update: "
    ).upper()

    for student in students:
        if student["matric_number"] == matric_number:
            print("\nStudent Found!")
            print("Press Enter to keep the current value.\n")

            new_name = input(
                f"Enter new name [{student['name']}]: "
            ).strip()

            new_department = input(
                f"Enter new department [{student['department']}]: "
            ).strip()

            new_level = input(
                f"Enter new level [{student['level']}]: "
            ).strip()

            if new_name:
                student["name"] = new_name.title()

            if new_department:
                student["department"] = new_department.title()

            if new_level:
                if new_level in {"100", "200", "300", "400", "500", "600"}:
                    student["level"] = new_level
                else:
                    print("Invalid level. Level was not changed.")

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    """Delete a student after confirmation."""
    print("\n--- Delete Student ---")

    matric_number = get_non_empty_input(
        "Enter matric number of student to delete: "
    ).upper()

    for student in students:
        if student["matric_number"] == matric_number:
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Department: {student['department']}")
            print(f"Level: {student['level']}") 

            confirmation = input(
                "\nAre you sure you want to delete this student? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                students.remove(student)
                save_students()
                print("\nStudent deleted successfully!")
            else:
                print("\nDeletion cancelled.")

            return        

    print("Student not found.")


def main():
    """Run the main application menu."""
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()