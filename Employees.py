
class Employee: #creating a class student
    def __init__(self, name, age, salary, isworking):
        """
        The __init__ method initializes the attributes of the Employee class.

        Parameters:
        name (str): The name of the employee.
        age (int): The age of the employee.
        salary (float): The salary of the employee.
        isworking (bool): The working status of the employee.
        """
        self.name = name  # Initialize the name attribute of employee , means the actual object name will be the name they pass in
        self.age = age  # Initialize the age attribute
        self.salary = salary  # Initialize the salary attribute
        self.isworking = isworking  # Initialize the isworking attribute

# This file defines the Employee class with attributes for name, age, salary, and isworking status.
