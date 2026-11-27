class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


# Creating an object
s1 = Student("Prabhas", 101)

# Accessing attributes
print("Name:", s1.name)
print("Roll Number:", s1.roll_no)

# Accessing method
s1.display()