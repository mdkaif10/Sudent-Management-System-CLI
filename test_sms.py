import unittest
from database import Database
from validators import *
import os

class TestStudentManagementSystem(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_school.db"
        self.db = Database(self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_student(self):
        student_id = self.db.add_student("John Doe", "2000-01-01", "1234567890")
        self.assertIsNotNone(student_id)
        student = self.db.get_student(student_id)
        self.assertEqual(student[1], "John Doe")

    def test_update_student(self):
        student_id = self.db.add_student("John Doe", "2000-01-01", "1234567890")
        success = self.db.update_student(student_id, "Jane Doe", "2000-01-01", "9876543210")
        self.assertTrue(success)
        student = self.db.get_student(student_id)
        self.assertEqual(student[1], "Jane Doe")

    def test_delete_student(self):
        student_id = self.db.add_student("John Doe", "2000-01-01", "1234567890")
        success = self.db.delete_student(student_id)
        self.assertTrue(success)
        student = self.db.get_student(student_id)
        self.assertIsNone(student)

    def test_add_grade(self):
        student_id = self.db.add_student("John Doe", "2000-01-01", "1234567890")
        self.db.add_grade(student_id, "Math", "A")
        grades = self.db.get_student_grades(student_id)
        self.assertEqual(len(grades), 1)
        self.assertEqual(grades[0][1], "A")

    def test_mark_attendance(self):
        student_id = self.db.add_student("John Doe", "2000-01-01", "1234567890")
        self.db.mark_attendance(student_id, "PRESENT")
        attendance = self.db.get_attendance_record(student_id)
        self.assertEqual(len(attendance), 1)
        self.assertEqual(attendance[0][1], "PRESENT")

    def test_validators(self):
        self.assertTrue(validate_date("2000-01-01"))
        self.assertFalse(validate_date("2000-13-01"))
        self.assertTrue(validate_contact("1234567890"))
        self.assertFalse(validate_contact("abc123"))
        self.assertTrue(validate_grade("A"))
        self.assertFalse(validate_grade("X"))
        self.assertTrue(validate_attendance_status("PRESENT"))
        self.assertFalse(validate_attendance_status("INVALID"))

if __name__ == '__main__':
    unittest.main()