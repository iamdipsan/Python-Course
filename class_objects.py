
from Employees import Employee  #This line means from Employees.py import the Employee class.

# Create an instance of the Employee class with name "Kimmy", age 45, salary 30000, and status "is working"
employee1 = Employee("Kimmy", 45, 30000, True)

# Create an instance of the Employee class with name "Jim", age 30, salary 60000, and status "is not working"
employee2 = Employee("Jim", 30, 60000, False)

# Print the name of the first employee
print(employee1.name)  # Output: Kimmy

# Print the name of the second employee
print(employee2.name)  # Output: Jim

# Print the age of the first employee
print(employee1.age)  # Output: 45

# Print the age of the second employee
print(employee2.age)  # Output: 30

# This file creates instances of the Employee class and prints the name and age of each employee.
