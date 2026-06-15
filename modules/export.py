# export.py
# Handles exporting data to CSV files.

import csv
import os
import sys
from datetime import datetime
sys.path.append(os.path.dirname(__file__))
from db import get_connection


def get_export_path(filename):
    # Build the full path to the exports folder.
    # datetime.now() adds a timestamp so files don't overwrite each other.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exports_dir = os.path.join(os.path.dirname(__file__), '..', 'exports')
    return os.path.join(exports_dir, f"{filename}_{timestamp}.csv")


def export_employees():
    sql = """
        SELECT employees.id, employees.name, employees.email,
               employees.role, departments.name AS department,
               employees.hire_date, employees.status
        FROM employees
        JOIN departments ON employees.department_id = departments.id
        ORDER BY employees.id
    """
    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No employees to export.")
        return

    filepath = get_export_path("employees")

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the header row first
        writer.writerow(["ID", "Name", "Email", "Role", "Department", "Hire Date", "Status"])
        # Write each employee as a row
        for row in rows:
            writer.writerow([row['id'], row['name'], row['email'],
                            row['role'], row['department'],
                            row['hire_date'], row['status']])

    print(f"Employees exported to: {filepath}")


def export_analytics():
    filepath = get_export_path("analytics")

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)

        # Section 1 — Headcount
        writer.writerow(["HEADCOUNT BY DEPARTMENT"])
        writer.writerow(["Department", "Total Employees"])
        conn = get_connection()
        for row in conn.execute("""
            SELECT departments.name, COUNT(employees.id) AS total
            FROM departments
            LEFT JOIN employees ON departments.id = employees.department_id
            GROUP BY departments.id
            ORDER BY total DESC
        """).fetchall():
            writer.writerow([row['name'], row['total']])
        conn.close()

        # Blank row between sections
        writer.writerow([])

        # Section 2 — Average salary
        writer.writerow(["AVERAGE SALARY BY DEPARTMENT"])
        writer.writerow(["Department", "Average Salary"])
        conn = get_connection()
        for row in conn.execute("""
            SELECT departments.name, ROUND(AVG(salaries.amount), 2) AS avg_salary
            FROM salaries
            JOIN employees ON salaries.employee_id = employees.id
            JOIN departments ON employees.department_id = departments.id
            GROUP BY departments.id
            ORDER BY avg_salary DESC
        """).fetchall():
            writer.writerow([row['name'], row['avg_salary']])
        conn.close()

        # Blank row between sections
        writer.writerow([])

        # Section 3 — Hires per year
        writer.writerow(["HIRES PER YEAR"])
        writer.writerow(["Year", "Total Hires"])
        conn = get_connection()
        for row in conn.execute("""
            SELECT STRFTIME('%Y', hire_date) AS year, COUNT(*) AS total
            FROM employees
            GROUP BY year
            ORDER BY year ASC
        """).fetchall():
            writer.writerow([row['year'], row['total']])
        conn.close()

    print(f"Analytics exported to: {filepath}")