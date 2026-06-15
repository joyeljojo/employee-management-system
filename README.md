# Employee Management & Analytics System

A command-line application built with Python and SQL to manage employee data and generate business analytics.

---

## What it does

- Add and manage departments and employees
- View all employees with their department information
- Update employee roles and status
- Generate business analytics reports:
  - Headcount by department
  - Average salary by department
  - Top earners
  - Hiring trends by year
  - Active vs inactive employees

---

## Tech stack

- **Python 3.8+**
- **SQLite** — embedded relational database
- **sqlite3** — Python standard library module

---

## Project structure

employee_system/

├── database/

│   └── schema.sql        # Database table definitions

├── modules/

│   ├── db.py             # Database connection and initialization

│   ├── employees.py      # Employee CRUD operations

│   └── analytics.py      # Business analytics queries

├── exports/              # Export outputs (CSV, charts)

├── main.py               # Application entry point

└── requirements.txt      # Project dependencies

---

## How to run

**1. Clone the repository**
**2. Initialize the database**
**3. Run the application**

---

## Key concepts demonstrated

- Relational database design with foreign keys
- SQL queries including JOINs, GROUP BY, and aggregate functions
- Python modular architecture — separation of concerns
- CRUD operations (Create, Read, Update, Delete)
- Protection against SQL injection using parameterized queries
- CLI interface with input validation

---

## Author

Joyel Jojo 
