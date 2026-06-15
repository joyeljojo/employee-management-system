-- schema.sql
-- SQL used CREATE TABLE to define the structure of your data.
-- Think of a table like a spreadsheet with a fixed column types.

-- IF NOT EXISTS means: only create this if it doesn't already exist.
-- This prevents errors if we run this more than once.

-- TABLE 1: departments
-- Every employee belongs to a department, so we create this first.
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- INTEGER = whole number. PRIMARY KEY = unique identifier for each row.
    -- AUTOINCREMENT = database automatically assigns 1, 2, 3... we don't do it manually.

    name TEXT NOT NULL UNIQUE,
    -- TEXT = any text. NOT NULL = this field cannot be empty. UNIQUE = no two departments can have the same name.

    location TEXT NOT NULL
);

-- TABLE 2: employees
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_id INTEGER NOT NULL,
    -- This will store the 'id' from the departments table.
    -- This is how we LINK two tables together.

    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL,
    hire_date TEXT NOT NULL,
    -- We store dates as text in 'YYYY-MM-DD' format. Example: '2024-01-15'

    status TEXT NOT NULL DEFAULT 'active',
    -- DEFAULT means: if we don't provide this value, use 'active' automatically.

    FOREIGN KEY (department_id) REFERENCES departments(id)
    -- FOREIGN KEY = this column must match a valid 'id' in the departments table.
    -- This prevents adding an employee to a department that doesn't exist.
);

-- TABLE 3: salaries
-- Separate table so we can keep salary history over time.
CREATE TABLE IF NOT EXISTS salaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    -- REAL = decimal number. Example: 75000.00

    effective_date TEXT NOT NULL,
    -- The date this salary became active.

    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
