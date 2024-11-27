student = {"name": "John", "age": 20, "grade": "A"}
sorted_dict = dict(sorted(student.items(), key=lambda item: item[1]))
print(sorted_dict)
