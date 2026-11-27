# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Creating objects
a = Animal()
d = Dog()

# Calling methods
a.sound()
d.sound()