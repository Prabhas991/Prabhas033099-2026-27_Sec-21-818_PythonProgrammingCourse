# Unit-2A_Task-1_Valid_Triangle_Angles.py

def check_triangle(angle1, angle2, angle3):
    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
        return "The triangle is valid."
    else:
        return "The triangle is not valid."

# Input from user
a1 = float(input("Enter first angle: "))
a2 = float(input("Enter second angle: "))
a3 = float(input("Enter third angle: "))

print(check_triangle(a1, a2, a3))