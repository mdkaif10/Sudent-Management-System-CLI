import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="school.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    dob DATE NOT NULL,
                    contact TEXT
                )
            ''')
            
            # Create grades table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    course TEXT NOT NULL,
                    grade TEXT NOT NULL,
                    date DATE NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students (id)
                )
            ''')
            
            # Create attendance table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    date DATE NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students (id)
                )
            ''')
            
            conn.commit()

    def add_student(self, name, dob, contact):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, dob, contact) VALUES (?, ?, ?)",
                (name, dob, contact)
            )
            return cursor.lastrowid

    def get_student(self, student_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            return cursor.fetchone()

    def update_student(self, student_id, name, dob, contact):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name = ?, dob = ?, contact = ? WHERE id = ?",
                (name, dob, contact, student_id)
            )
            return cursor.rowcount > 0

    def delete_student(self, student_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            return cursor.rowcount > 0

    def add_grade(self, student_id, course, grade):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute(
                "INSERT INTO grades (student_id, course, grade, date) VALUES (?, ?, ?, ?)",
                (student_id, course, grade, date)
            )

    def get_student_grades(self, student_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT course, grade, date FROM grades WHERE student_id = ?",
                (student_id,)
            )
            return cursor.fetchall()

    def mark_attendance(self, student_id, status):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            date = datetime.now().strftime("%Y-%m-%d")
            cursor.execute(
                "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                (student_id, date, status)
            )

    def get_attendance_record(self, student_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT date, status FROM attendance WHERE student_id = ?",
                (student_id,)
            )
            return cursor.fetchall()

    def search_students(self, query):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM students WHERE name LIKE ? OR id = ?",
                (f"%{query}%", query if query.isdigit() else -1)
            )
            return cursor.fetchall()