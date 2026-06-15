# main.py
import sys
sys.path.append('modules')

from employees import (
    add_department, add_employee, get_all_employees,
    get_employee_by_id, update_employee_role,
    deactivate_employee, get_all_departments
)
from analytics import (
    headcount_by_department, average_salary_by_department,
    top_earners, hires_per_year, active_vs_inactive
)
from export import export_employees, export_analytics


def print_divider():
    print("\n" + "=" * 40)


def show_main_menu():
    print_divider()
    print(" Employee Management System")
    print("=" * 40)
    print(" 1. Add Department")
    print(" 2. Add Employee")
    print(" 3. View All Employees")
    print(" 4. View Single Employee")
    print(" 5. Update Employee Role")
    print(" 6. Deactivate Employee")
    print(" 7. View Analytics")
    print(" 8. Export Data")
    print(" 9. Exit")
    print("=" * 40)


def handle_add_department():
    print("\n-- Add Department --")
    name = input("Department name: ")
    location = input("Location: ")
    add_department(name, location)


def handle_add_employee():
    print("\n-- Add Employee --")
    print("\nExisting departments:")
    departments = get_all_departments()
    for dept in departments:
        print(f"  ID {dept['id']} -> {dept['name']} ({dept['location']})")
    print()
    name = input("Employee name: ")
    email = input("Email: ")
    role = input("Role: ")
    department_id = int(input("Department ID: "))
    hire_date = input("Hire date (YYYY-MM-DD): ")
    add_employee(name, email, role, department_id, hire_date)


def handle_view_all_employees():
    print("\n-- All Employees --")
    employees = get_all_employees()
    if not employees:
        print("No employees found.")
        return
    print(f"\n{'ID':<5} {'Name':<20} {'Role':<25} {'Department':<15} {'Status'}")
    print("-" * 75)
    for emp in employees:
        print(f"{emp['id']:<5} {emp['name']:<20} {emp['role']:<25} {emp['department_name']:<15} {emp['status']}")


def handle_view_single_employee():
    print("\n-- View Single Employee --")
    employee_id = int(input("Enter employee ID: "))
    emp = get_employee_by_id(employee_id)
    if not emp:
        print("Employee not found.")
        return
    print(f"\nID:         {emp['id']}")
    print(f"Name:       {emp['name']}")
    print(f"Email:      {emp['email']}")
    print(f"Role:       {emp['role']}")
    print(f"Department: {emp['department_name']}")
    print(f"Hire Date:  {emp['hire_date']}")
    print(f"Status:     {emp['status']}")


def handle_update_role():
    print("\n-- Update Employee Role --")
    employee_id = int(input("Enter employee ID: "))
    new_role = input("Enter new role: ")
    update_employee_role(employee_id, new_role)


def handle_deactivate():
    print("\n-- Deactivate Employee --")
    employee_id = int(input("Enter employee ID: "))
    deactivate_employee(employee_id)


def handle_analytics():
    while True:
        print("\n-- Analytics --")
        print(" 1. Headcount by Department")
        print(" 2. Average Salary by Department")
        print(" 3. Top Earners")
        print(" 4. Hires Per Year")
        print(" 5. Active vs Inactive")
        print(" 6. Back to Main Menu")
        choice = input("\nChoose report: ")
        if choice == '1':
            print("\n-- Headcount by Department --")
            for row in headcount_by_department():
                print(f"  {row['department']:<20} → {row['total_employees']} employees")
        elif choice == '2':
            print("\n-- Average Salary by Department --")
            for row in average_salary_by_department():
                print(f"  {row['department']:<20} → ${row['avg_salary']}")
        elif choice == '3':
            print("\n-- Top Earners --")
            for row in top_earners():
                print(f"  {row['name']:<20} | {row['role']:<25} | ${row['salary']}")
        elif choice == '4':
            print("\n-- Hires Per Year --")
            for row in hires_per_year():
                print(f"  {row['year']} → {row['total_hires']} hires")
        elif choice == '5':
            print("\n-- Active vs Inactive --")
            for row in active_vs_inactive():
                print(f"  {row['status']:<10} → {row['total']}")
        elif choice == '6':
            break
        else:
            print("Invalid choice.")


def handle_export():
    print("\n-- Export Data --")
    print(" 1. Export Employees to CSV")
    print(" 2. Export Analytics to CSV")
    choice = input("\nChoose export: ")
    if choice == '1':
        export_employees()
    elif choice == '2':
        export_analytics()
    else:
        print("Invalid choice.")


def main():
    print("Starting Employee Management System...")
    while True:
        show_main_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            handle_add_department()
        elif choice == '2':
            handle_add_employee()
        elif choice == '3':
            handle_view_all_employees()
        elif choice == '4':
            handle_view_single_employee()
        elif choice == '5':
            handle_update_role()
        elif choice == '6':
            handle_deactivate()
        elif choice == '7':
            handle_analytics()
        elif choice == '8':
            handle_export()
        elif choice == '9':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-9.")


if __name__ == '__main__':
    main()