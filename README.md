# Student Record Management System

A desktop **Student Record Management System** developed with **Python Tkinter**.

## Features
- Add student records
- Display records in a Treeview table
- Update records
- Delete records
- Search by student ID
- Refresh records
- Automatic saving to `student.txt` and `student.csv`
- File handling and exception handling
- Full-screen GUI
- Student fields: ID, Name, Age, Course, City

## Technologies
- Python 3
- Tkinter
- CSV module
- File handling

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python student_record_management.py
```

Tkinter is included with most standard Python installations on Windows.

## Data Storage

The application stores records locally:
- `student.txt` - simple text format
- `student.csv` - structured CSV format

No SQL database is required.

## Project Background

This implementation is recreated from the submitted project report for the Student Record Management System. The report describes a Python Tkinter GUI with file-based persistence, student ID, name, age, course and city fields, and Add/Update/Delete/Search/Refresh functionality.
