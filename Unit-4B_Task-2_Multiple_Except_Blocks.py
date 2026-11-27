my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Element:", my_list[index])

except ValueError:
    print("Please enter an integer")

except IndexError:
    print("Index out of range")