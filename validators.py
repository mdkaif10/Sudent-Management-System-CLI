from datetime import datetime

def validate_date(date_str):
    try:
        return bool(datetime.strptime(date_str, "%Y-%m-%d"))
    except ValueError:
        return False

def validate_contact(contact):
    return contact.replace("-", "").replace("+", "").isdigit()

def validate_grade(grade):
    valid_grades = ['A', 'B', 'C', 'D', 'F']
    return grade.upper() in valid_grades

def validate_attendance_status(status):
    valid_status = ['PRESENT', 'ABSENT', 'LATE']
    return status.upper() in valid_status