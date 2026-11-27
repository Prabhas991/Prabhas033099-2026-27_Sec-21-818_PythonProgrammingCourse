class Student:
    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Branch:", self.branch)


# Creating an object
s1 = Student("Prabhas", 101, "CSE")

# Calling the method
s1.display()