# db.py
# This file has one job: manage the connection to our database.
import sqlite3
# sqlite3 is a built-in Python module. No installation needed.
# It lets Python talk to a SQLite database.

import os
# os is another built-in module.
# We use it to work with file paths on your computer.

# This line builds the path to where our database file will live.
# __file__ means "the current file (db.py)"
# os.path.dirname gets the folder that file is in
# os.path.join then builds the full path to our .db file
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'employee_system.db')

# What this means in plain English:
# "Go one folder up from modules/, then into database/, and use employee_system.db"
# The .db file doesn't exist yet — SQLite will create it automatically on first run.

def get_connection():
    # A function that opens a connection to the database and returns it.
    # Think of a "connection" like opening a phone call with the database.
    # You open it, do your work, then close it.

    conn = sqlite3.connect(DB_PATH)
    # This opens the connection.
    # If the .db file doesn't exist yet, SQLite creates it automatically.

    conn.row_factory = sqlite3.Row
    # This is important.
    # Normally SQLite returns rows as plain tuples: (1, "Alice", "Engineering")
    # With row_factory set, rows behave like dictionaries: {"id": 1, "name": "Alice"}
    # Much easier to work with in Python.

    return conn
    # Hand the connection back to whoever called this function.

def initialize_database():
    # This function creates our tables by running schema.sql.
    # We only need to call this ONCE — when setting up the project.

    schema_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'schema.sql')
    # Build the path to our schema.sql file.

    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    # Open schema.sql and read all its contents into a variable called schema_sql.
    # 'r' means read mode.
    # 'with open' automatically closes the file when done — good practice.

    conn = get_connection()
    # Open a connection to the database.

    conn.executescript(schema_sql)
    # Run all the SQL in schema.sql against the database.
    # executescript() runs multiple SQL statements at once.
    # This is what actually creates the 3 tables.

    conn.commit()
    # Save the changes permanently.
    # Without commit(), changes exist temporarily in memory but never get saved.

    conn.close()
    # Close the connection. Like hanging up the phone call.

    print("Database initialized successfully.")

if __name__ == "__main__":
    # This block only runs if you execute THIS file directly.
    # It will NOT run if another file imports db.py.
    # This is a standard Python pattern — very important to understand.

    initialize_database()