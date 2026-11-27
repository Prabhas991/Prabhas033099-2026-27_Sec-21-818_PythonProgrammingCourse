import mypackage.addition
import mypackage.subtraction
import mypackage.multiplication
import mypackage.division

a = 20
b = 10

print("First Number:", a)
print("Second Number:", b)

print("Addition:", mypackage.addition.add(a, b))
print("Subtraction:", mypackage.subtraction.sub(a, b))
print("Multiplication:", mypackage.multiplication.mul(a, b))
print("Division:", mypackage.division.div(a, b))