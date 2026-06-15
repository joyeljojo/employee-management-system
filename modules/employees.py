# employees.py
# This file handles all employee-related database operations.

import sys
import os
sys.path.append(os.path.dirname(__file__))
from db import get_connection

# ─────────────────────────────────────────
# CREATE — Add a new employee
# ─────────────────────────────────────────

def add_employee(name, email, role, department_id, hire_date):
    # This function takes employee details and saves them to the database.

    sql = """
        INSERT INTO employees (name, email, role, department_id, hire_date)
        VALUES (?, ?, ?, ?, ?)
    """
    # INSERT INTO = SQL command to add a new row to a table.
    # We list which columns we're filling in.
    # The ? marks are placeholders — we never put values directly into SQL.
    # This protects against SQL injection attacks (a real security issue).

    conn = get_connection()
    conn.execute(sql, (name, email, role, department_id, hire_date))
    # The second argument is a tuple of values.
    # SQLite replaces each ? with the corresponding value in order.
    conn.commit()
    conn.close()
    print(f"Employee '{name}' added successfully.")

# ─────────────────────────────────────────
# CREATE — Add a new department
# ─────────────────────────────────────────

def add_department(name, location):
    sql = """
        INSERT INTO departments (name, location)
        VALUES (?, ?)
    """
    conn = get_connection()
    conn.execute(sql, (name, location))
    conn.commit()
    conn.close()
    print(f"Department '{name}' added successfully.")

# ─────────────────────────────────────────
# READ — Get all employees
# ─────────────────────────────────────────

def get_all_employees():
    sql = """
        SELECT employees.id, employees.name, employees.email, employees.role, employees.hire_date, employees.status, departments.name AS department_name
        FROM employees
        JOIN departments ON employees.department_id = departments.id
    """
    # SELECT = choose which columns to return.
    # FROM employees = main table we're reading from.
    # JOIN departments = bring in matching data from departments table.
    # ON employees.department_id = departments.id = the matching rule.
    # AS department_name = rename the column in the result so it's clear.

    conn = get_connection()
    cursor = conn.execute(sql)
    # cursor is like a pointer that holds the results of the query.

    rows = cursor.fetchall()
    # fetchall() gets every matching row as a list.

    conn.close()
    return rows
    # Send the results back to whoever called this function.

# ─────────────────────────────────────────
# READ — Get one employee by ID
# ─────────────────────────────────────────

def get_employee_by_id(employee_id):
    sql = """
        SELECT employees.id, employees.name, employees.email,
               employees.role, employees.hire_date, employees.status,
               departments.name AS department_name
        FROM employees
        JOIN departments ON employees.department_id = departments.id
        WHERE employees.id = ?
    """
    conn = get_connection()
    cursor = conn.execute(sql, (employee_id,))
    row = cursor.fetchone()
    conn.close()
    return row

# ─────────────────────────────────────────
# UPDATE — Change an employee's role
# ─────────────────────────────────────────

def update_employee_role(employee_id, new_role):
    sql = """
        UPDATE employees
        SET role = ?
        WHERE id = ?
    """
    # UPDATE = modify existing rows.
    # SET = which column to change and what to change it to.
    # WHERE = which row to update. Without WHERE, ALL rows would be updated.

    conn = get_connection()
    conn.execute(sql, (new_role, employee_id))
    conn.commit()
    conn.close()
    print(f"Employee {employee_id} role updated to '{new_role}'.")

# ─────────────────────────────────────────
# UPDATE — Change employee status
# ─────────────────────────────────────────

def deactivate_employee(employee_id):
    sql = """
        UPDATE employees
        SET status = 'inactive'
        WHERE id = ?
    """
    conn = get_connection()
    conn.execute(sql, (employee_id,))
    conn.commit()
    conn.close()
    print(f"Employee {employee_id} deactivated.")

# ─────────────────────────────────────────
# READ — Get all departments
# ─────────────────────────────────────────

def get_all_departments():
    sql = "SELECT * FROM departments"
    # SELECT * means return ALL columns.
    
    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

