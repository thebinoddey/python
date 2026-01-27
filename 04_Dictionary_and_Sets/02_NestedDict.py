student = {
    "name": "Dhruv",
    "age": 23,
    "courses": {
        "Math": 85,
        "Physics": 90,
        "Chemistry": 85
    }
        
}
print(student)
print(student["courses"]["Physics"])

#Methods
print(student.keys())
print(list(student.keys()))
print(len(student))
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("address"))
print(student.setdefault("address", "Unknown"))
print(student)
print(student.pop("age"))
print(student)
print(student.popitem())
print(student)
print(student.update({"name": "Dhruv Kumar", "age": 24}))
print(student)