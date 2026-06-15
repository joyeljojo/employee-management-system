# analytics.py
# This file answers business questions by querying the database.

import sys
import os
sys.path.append(os.path.dirname(__file__))
from db import get_connection

# ─────────────────────────────────────────
# How many employees in each department?
# ─────────────────────────────────────────

def headcount_by_department():
    sql = """
        SELECT departments.name AS department,
               COUNT(employees.id) AS total_employees
        FROM departments
        LEFT JOIN employees on departments.id = employees.department_id
        GROUP BY departments.id
        ORDER BY total_employees DESC
    """
    # LEFT JOIN = include ALL departments even if they have zero employees.
    # Regular JOIN skips departments with no employees.
    # GROUP BY departments.id = count employees per department separately.
    # ORDER BY total_employees DESC = sort highest to lowest.

    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

# ─────────────────────────────────────────
# Average salary per department
# ─────────────────────────────────────────

def average_salary_by_department():
    sql = """
        SELECT departments.name AS department,
               ROUND (AVG(salaries.amount), 2) AS avg_salary
        FROM salaries
        JOIN employees ON salaries.employee_id = employees.id
        JOIN departments ON employees.department_id = departments.id
        GROUP BY departments.id
        ORDER BY avg_salary DESC
    """
    # ROUND(AVG(salaries.amount), 2) = average salary rounded to 2 decimal places.
    # Two JOINs here — salaries links to employees, employees links to departments.
    # This is how you connect 3 tables together.

    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

# ─────────────────────────────────────────
# Top 5 highest paid employees
# ─────────────────────────────────────────

def top_earners(limit=5):
    sql = """
        SELECT employees.name,
               employees.role,
               departments.name AS department,
               salaries.amount AS salary
        FROM salaries
        JOIN employees ON salaries.employee_id = employees.id
        JOIN departments ON employees.department_id = departments.id
        ORDER BY salaries.amount DESC
        LIMIT ?
    """
    # ORDER BY salary DESC = highest salary first.
    # LIMIT = only return the top N rows.

    conn = get_connection()
    cursor = conn.execute(sql, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ─────────────────────────────────────────
# How many employees hired per year?
# ─────────────────────────────────────────

def hires_per_year():
    sql = """
        SELECT STRFTIME('%Y', hire_date) AS year,
               COUNT(*) AS total_hires
        FROM employees
        GROUP BY year
        ORDER BY year ASC
    """
    # STRFTIME('%Y', hire_date) = extract just the year from the date.
    # Example: '2023-01-15' becomes '2023'.
    # GROUP BY year = count hires per year separately.
    
    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

# ─────────────────────────────────────────
# Active vs inactive employee count
# ─────────────────────────────────────────

def active_vs_inactive():
    sql = """
        SELECT status,
               COUNT(*) AS total
        FROM employees
        GROUP BY status
    """
    # GROUP BY status splits employees into 'active' and 'inactive' groups.
    # COUNT(*) counts each group separately.

    conn = get_connection()
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows