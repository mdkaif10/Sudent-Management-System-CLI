
# Student Management System

A Python-based application for managing student academic records such as grades, attendance, and personal details using SQLite. The application supports adding, updating, and retrieving student data efficiently.

---

## Features

- **Add Student Records**: Input student details like name, address, grades, and attendance.
- **Update Records**: Modify existing student information.
- **Retrieve Records**: View and search for specific student details.
- **Database Management**: Uses SQLite for lightweight and efficient data storage.
- **User Interface**: Supports both CLI and GUI for interacting with the system.

---

## Tech Stack

- **Programming Language**: Python
- **Database**: SQLite
- **CLI Framework**: Python's built-in libraries
- **Version Control**: Git and GitHub

---

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python (version 3.7 or later)
- SQLite3 (comes pre-installed with Python)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mdkaif10/Sudent-Management-System-CLI.git
   cd student-management-system
   ```

2. **Install Dependencies**  
   If you use additional libraries (e.g., Pandas, ReportLab):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   - For CLI:
     ```bash
     python main.py
     ```

---

## Database Schema

The database is managed using SQLite. You can create the database by running the initialization script:
```python
import sqlite3

def initialize_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        grade TEXT
    )''')
    conn.commit()
    conn.close()

initialize_db()
```

---
## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.


---

## Author

Developed by **Md Kaif**  
Contact: [Email](mailto:md.71.kaif@gmail.com) or [GitHub Profile](https://github.com/mdkaif10)

---

## Download

Click [here](https://github.com/mdkaif10/Sudent-Management-System-CLI/archive/refs/heads/main.zip) to download the project.

---
