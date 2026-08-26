import json


FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


students = load_students()


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty. Please try again.")


def get_level():
    while True:
        level = input("Enter level: ").strip()

        if level.isdigit() and int(level) > 0:
            return level

        print("Please enter a valid level, such as 100, 200, 300, or 400.")


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    print("\n--- Add Student ---")

    name = get_non_empty_input("Enter student name: ")
    matric_number = get_non_empty_input("Enter matric number: ")
    department = get_non_empty_input("Enter department: ")
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
    print("\n--- Search Student ---")

    matric_number = input("Enter matric number: ").strip()

    for student in students:
        if student["matric_number"] == matric_number:
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Matric Number: {student['matric_number']}")
            print(f"Department: {student['department']}")
            print(f"Level: {student['level']}")
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    matric_number = input(
        "Enter matric number of student to update: "
    ).strip()

    for student in students:
        if student["matric_number"] == matric_number:
            print("\nStudent Found!")
            print("Leave a field empty if you don't want to change it.")

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
                student["name"] = new_name

            if new_department:
                student["department"] = new_department

            if new_level:
                if new_level.isdigit() and int(new_level) > 0:
                    student["level"] = new_level
                else:
                    print("Invalid level. Level was not changed.")

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    matric_number = input(
        "Enter matric number of student to delete: "
    ).strip()

    for student in students:
        if student["matric_number"] == matric_number:
            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
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


main()