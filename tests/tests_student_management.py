import unittest
from unittest.mock import patch
import student_management


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.original_students = student_management.students
        student_management.students = []

    def tearDown(self):
        student_management.students = self.original_students

    @patch(
        "builtins.input",
        side_effect=[
            "John Doe",
            "ABC123",
            "Computer Science",
            "300"
        ]
    )
    @patch("student_management.save_students")
    def test_add_student(self, mock_save, mock_input):
        student_management.add_student()

        self.assertEqual(len(student_management.students), 1)
        self.assertEqual(
            student_management.students[0]["name"],
            "John Doe"
        )
        self.assertEqual(
            student_management.students[0]["matric_number"],
            "ABC123"
        )
        self.assertEqual(
            student_management.students[0]["department"],
            "Computer Science"
        )
        self.assertEqual(
            student_management.students[0]["level"],
            "300"
        )

        mock_save.assert_called_once()

    @patch(
        "builtins.input",
        side_effect=[
            "John Doe",
            "ABC123",
            "Computer Science",
            "300"
        ]
    )
    @patch("student_management.save_students")
    def test_duplicate_student(self, mock_save, mock_input):
        student_management.add_student()

        mock_input.side_effect = [
            "Jane Doe",
            "ABC123",
            "Cybersecurity",
            "400"
        ]

        student_management.add_student()

        self.assertEqual(len(student_management.students), 1)

    def test_search_student(self):
        student_management.students.append({
            "name": "Jane Doe",
            "matric_number": "XYZ456",
            "department": "Cybersecurity",
            "level": "400"
        })

        found_student = next(
            (
                student
                for student in student_management.students
                if student["matric_number"] == "XYZ456"
            ),
            None
        )

        self.assertIsNotNone(found_student)
        self.assertEqual(found_student["name"], "Jane Doe")

    @patch(
        "builtins.input",
        side_effect=[
            "ABC123",
            "Jane Doe",
            "Cybersecurity",
            "400"
        ]
    )
    @patch("student_management.save_students")
    def test_update_student(self, mock_save, mock_input):
        student_management.students.append({
            "name": "John Doe",
            "matric_number": "ABC123",
            "department": "Computer Science",
            "level": "300"
        })

        student_management.update_student()

        self.assertEqual(
            student_management.students[0]["name"],
            "Jane Doe"
        )
        self.assertEqual(
            student_management.students[0]["department"],
            "Cybersecurity"
        )
        self.assertEqual(
            student_management.students[0]["level"],
            "400"
        )

        mock_save.assert_called_once()

    @patch(
        "builtins.input",
        side_effect=["ABC123", "y"]
    )
    @patch("student_management.save_students")
    def test_delete_student(self, mock_save, mock_input):
        student_management.students.append({
            "name": "John Doe",
            "matric_number": "ABC123",
            "department": "Computer Science",
            "level": "300"
        })

        student_management.delete_student()

        self.assertEqual(len(student_management.students), 0)
        mock_save.assert_called_once()


if __name__ == "__main__":
    unittest.main()