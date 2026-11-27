student = {"name": "Krishna", "age": 20, "course": "B.Tech"}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Get:", student.get("name"))

student.update({"age": 21})
print("After Update:", student)

student.pop("course")
print("After Pop:", student)