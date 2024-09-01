# Import the Student class from the Student module
from Student import Student

# Create Student objects with name, major, and GPA
student1 = Student("Dipsan", "Computer Science", 3.9)  # Student with a GPA of 3.9
student2 = Student("Luffy", "Electrical Engineering", 3.1)  # Student with a GPA of 3.9

# Print whether each student is considered a good student
print(student1.good_student())  # Should print True since GPA is 3.9
print(student2.good_student())  # Should print True since GPA is 3.9
