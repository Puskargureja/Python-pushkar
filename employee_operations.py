"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
    id = int(input("please enter the ID for the new employee:")
    firstName = input("please enter the employee's firstname")
    last_name = input("please enter the employee's lastname")
    date_of_birth = input("please enter the employee's date of birth in YYYY/MM/DD")
    start_of_year = int(input("please enter the employee's starting year")
    position = input("please enter the employee's position")
    salary = float(input("please enter the employee's salary")
    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """

def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    def get_departments():
    pass


departments = get_departments()


def get_employees():
    pass


employees = get_employees()
print("List of Departments:")
for department in departments:
    print(department)

    print("\nList of Employees:")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['name']}, Department: {employee['department']}")
        
        print("\nList of Departments with Average Age and Salary:")
    
def calculate_department_stats(employees, department):
    pass


for department in departments:
        avg_age, avg_salary = calculate_department_stats(employees, department)
print(f"Department: {department}, Average Age: {avg_age}, Average Salary: {avg_salary}")

print("\nEmployees in Each Department:")
for department in departments:
        print(f"\nDepartment: {department}")
        department_employees = [employee for employee in employees if employee['department'] == department]
        total_salary = sum(employee['salary'] for employee in department_employees)
        for employee in department_employees
            print(
                f"ID: {employee['id']}, Name: {employee['name']}, Date of Birth: {employee['dob']}, Salary: {employee['salary']}, Total Salary for Department: {total_salary}")
def get_departments():
    return ["Analyst", "Engineer", "Manager"]


def get_employees():
    return [
        {"id": 1, "name": "Jane Doe", "department": "Manager", "dob": "1980-05-15", "salary": 160000},
        {"id": 2, "name": "John Smith", "department": "Engineer", "dob": "1975-12-20", "salary": 90000},
        {"id": 3, "name": "Alice Johnson", "department": "Analyst", "dob": "1990-08-10", "salary": 75000},
    ]


def calculate_department_stats(employees, department):
    department_employees = [employee for employee in employees if employee['department'] == department]
    if len(department_employees) == 0:
        return 0, 0
    avg_age = sum(get_age(employee['dob']) for employee in department_employees) / len(department_employees)
    avg_salary = sum(employee['salary'] for employee in department_employees) / len(department_employees)
    return avg_age, avg_salary


def get_age(date_of_birth):
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
