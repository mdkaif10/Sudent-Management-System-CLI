from database import Database
from validators import *
import sys

class StudentManagementSystem:
    def __init__(self):
        self.db = Database()

    def display_menu(self):
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Grade")
        print("6. View Grades")
        print("7. Mark Attendance")
        print("8. View Attendance")
        print("9. Search Students")
        print("0. Exit")

    def get_student_info(self):
        name = input("Enter student name: ")
        while True:
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            if validate_date(dob):
                break
            print("Invalid date format!")

        while True:
            contact = input("Enter contact number: ")
            if validate_contact(contact):
                break
            print("Invalid contact number!")

        return name, dob, contact

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ")

            if choice == "1":
                name, dob, contact = self.get_student_info()
                student_id = self.db.add_student(name, dob, contact)
                print(f"Student added successfully! ID: {student_id}")

            elif choice == "2":
                student_id = input("Enter student ID: ")
                student = self.db.get_student(student_id)
                if student:
                    print(f"ID: {student[0]}")
                    print(f"Name: {student[1]}")
                    print(f"DOB: {student[2]}")
                    print(f"Contact: {student[3]}")
                else:
                    print("Student not found!")

            elif choice == "3":
                student_id = input("Enter student ID: ")
                if self.db.get_student(student_id):
                    name, dob, contact = self.get_student_info()
                    if self.db.update_student(student_id, name, dob, contact):
                        print("Student updated successfully!")
                else:
                    print("Student not found!")

            elif choice == "4":
                student_id = input("Enter student ID: ")
                if self.db.delete_student(student_id):
                    print("Student deleted successfully!")
                else:
                    print("Student not found!")

            elif choice == "5":
                student_id = input("Enter student ID: ")
                if self.db.get_student(student_id):
                    course = input("Enter course name: ")
                    while True:
                        grade = input("Enter grade (A-F): ").upper()
                        if validate_grade(grade):
                            break
                        print("Invalid grade!")
                    self.db.add_grade(student_id, course, grade)
                    print("Grade added successfully!")
                else:
                    print("Student not found!")

            elif choice == "6":
                student_id = input("Enter student ID: ")
                grades = self.db.get_student_grades(student_id)
                if grades:
                    for course, grade, date in grades:
                        print(f"Course: {course}, Grade: {grade}, Date: {date}")
                else:
                    print("No grades found!")

            elif choice == "7":
                student_id = input("Enter student ID: ")
                if self.db.get_student(student_id):
                    while True:
                        status = input("Enter status (PRESENT/ABSENT/LATE): ").upper()
                        if validate_attendance_status(status):
                            break
                        print("Invalid status!")
                    self.db.mark_attendance(student_id, status)
                    print("Attendance marked successfully!")
                else:
                    print("Student not found!")

            elif choice == "8":
                student_id = input("Enter student ID: ")
                attendance = self.db.get_attendance_record(student_id)
                if attendance:
                    for date, status in attendance:
                        print(f"Date: {date}, Status: {status}")
                else:
                    print("No attendance records found!")

            elif choice == "9":
                query = input("Enter student name or ID to search: ")
                students = self.db.search_students(query)
                if students:
                    for student in students:
                        print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}, Contact: {student[3]}")
                else:
                    print("No students found!")

            elif choice == "0":
                print("Goodbye!")
                sys.exit(0)

            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()