dict1 = {"name": "Krishna", "age": 20}
dict2 = {"city": "Guntur", "course": "B.Tech"}

merged = dict1.copy()
merged.update(dict2)

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)