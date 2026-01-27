# key : value
#unordered, mutable, and don't allow duplicate keys

info = {
    "Name" : "Binod Dey",
    "Age" : 19,
    "City" : "Jaipur",
    "Country" : "India"
}

print(info)
print(info["Name"])

info["Age"] = 20
print(info)

info["Profession"] = "Student"
print(info)

null_dict = {}
print(null_dict)