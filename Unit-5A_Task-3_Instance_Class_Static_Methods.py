class Student:
    school = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

    # Class Method
    @classmethod
    def show_school(cls):
        print("School:", cls.school)

    # Static Method
    @staticmethod
    def message():
        print("Welcome to Python Programming!")


# Creating an object
s1 = Student("Prabhas", 101)

# Calling methods
s1.display()
Student.show_school()
Student.message()