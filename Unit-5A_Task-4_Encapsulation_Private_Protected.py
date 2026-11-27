class Student:
    def __init__(self, name, age, marks):
        self.name = name       # Public attribute
        self._age = age        # Protected attribute
        self.__marks = marks   # Private attribute

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Marks:", self.__marks)


# Creating an object
s1 = Student("Prabhas", 18, 95)

# Accessing attributes
print("Name:", s1.name)
print("Age:", s1._age)

# Accessing private attribute through a method
s1.display()