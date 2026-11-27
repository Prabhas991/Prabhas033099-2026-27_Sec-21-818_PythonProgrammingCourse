class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, age):
        self.__age = age

# Creating an object
s1 = Student("Prabhas", 18)

# Accessing value using getter
print("Age:", s1.get_age())

# Updating value using setter
s1.set_age(20)

# Display updated value
print("Updated Age:", s1.get_age())