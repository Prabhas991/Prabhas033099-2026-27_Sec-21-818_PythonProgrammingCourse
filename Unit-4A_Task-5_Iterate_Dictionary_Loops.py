marks = {
    "Python": 90,
    "Maths": 85,
    "English": 80
}

print("Keys:")
for key in marks.keys():
    print(key)

print("Values:")
for value in marks.values():
    print(value)

print("Items:")
for key, value in marks.items():
    print(key, ":", value)