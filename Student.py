# Define a class to represent a student with attributes and methods
class Student:
    # Initialize the Student object with name, major, and GPA
    def __init__(self, name, major, gpa):
        self.name = name  # Student's name
        self.major = major  # Student's major field of study
        self.gpa = gpa  # Student's GPA
    
    # Method to determine if the student is a good student based on GPA
    def good_student(self):
        # Return True if GPA is 3.5 or higher, otherwise return False
        if self.gpa >= 3.5:
            return True
        else:
            return False
