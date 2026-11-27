students = {
    1: {"name": "Krishna", "marks": 90},
    2: {"name": "Rahul", "marks": 85},
    3: {"name": "Arjun", "marks": 95}
}

for roll, details in students.items():
    print("Roll Number:", roll)
    print("Name:", details["name"])
    print("Marks:", details["marks"])