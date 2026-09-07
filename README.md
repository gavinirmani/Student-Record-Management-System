# 🎓 Student Record Management System

A desktop-based **Student Record Management System** developed using **Python and Tkinter**. The application provides a simple and user-friendly graphical interface for managing student information.

## 📌 Project Overview

The Student Record Management System is designed to make student record management easier and more efficient. Users can add, view, update, delete, search, and refresh student records through a graphical user interface.

The system stores student information using **text and CSV files**, so no SQL database installation is required.

## ✨ Features

* ➕ Add new student records
* 👁️ Display student records in a table
* ✏️ Update existing records
* 🗑️ Delete student records
* 🔍 Search students by ID
* 🔄 Refresh records
* 💾 Automatically save records
* 📄 Store data in TXT format
* 📊 Store data in CSV format
* 🖥️ Full-screen graphical interface
* ⚠️ Exception and input validation handling

## 📝 Student Information

The system manages the following information:

| Field  | Description                   |
| ------ | ----------------------------- |
| ID     | Unique student identification |
| Name   | Student's name                |
| Age    | Student's age                 |
| Course | Student's course              |
| City   | Student's city                |

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **CSV Module** – Structured data storage
* **File Handling** – Reading and writing records
* **Exception Handling** – Error management

## 📂 Project Structure

```text
Student-Record-Management-System/
│
├── student_record_management.py
├── student.csv
├── student.txt
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Record-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Student-Record-Management-System
```

### 3. Run the Application

```bash
python student_record_management.py
```

The Tkinter application will open automatically.

## 💾 Data Storage

The application uses two files to store student records:

### `student.txt`

Stores records in a simple text format:

```text
ID | Name | Age | Course | City
```

### `student.csv`

Stores records in structured CSV format, making the data easy to view and process using spreadsheet applications.

## 🖥️ Application Workflow

```text
Enter Student Details
        ↓
     Click Add
        ↓
Record Added to Table
        ↓
Automatically Saved
        ↓
 student.txt + student.csv
```

Users can also select an existing record to **update or delete** it, and search for records using the student ID.

## 🧠 Python Concepts Demonstrated

This project demonstrates several fundamental Python programming concepts:

* Functions
* Object-Oriented Programming
* Event Handling
* GUI Development
* File Handling
* CSV File Processing
* Lists
* Strings
* Tuples
* Exception Handling
* Input Validation

## ⚠️ Exception Handling

The application uses `try-except` blocks to handle common errors, including:

* Invalid age input
* Empty fields
* File errors
* Invalid data

This helps prevent application crashes and improves the user experience.

## 🔮 Future Improvements

Possible future enhancements include:

* 🔐 User login system
* ✅ Advanced data validation
* ↕️ Record sorting
* 💾 Automatic backup system
* 📤 Excel data export
* 🗄️ Database integration

## 🎯 Purpose

This project was developed to demonstrate practical knowledge of **Python programming, GUI application development, file management, and event-driven programming**.

## 👩‍💻 Author

**K.G.G. Nirmani**

**Course:** BSc. (Hons) in Data Science
**Module:** CCS1300 – Programming Concepts (GUI Application Development)

## 📄 License

This project is intended for educational and academic purposes.

