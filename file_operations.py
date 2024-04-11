"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
   def read_employees():
    
    with open('employees.txt', 'r') as file:

        employees_data = file.readlines()


    employees_data = [employee.strip() for employee in employees_data]

 
    return employees_data
       
def write_employees(employees_data):
 with open('employees.txt', 'w') as file:
        for employee in employees_data:
            file.write(f"{employee}\n") 
            """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """

