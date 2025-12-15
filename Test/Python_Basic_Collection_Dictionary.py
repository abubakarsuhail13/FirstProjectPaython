my_dict = {
    "Class" : "IT",
    "Name" : "Python",
    "Age" : 30
}

print(my_dict)
print(my_dict["Name"])
print(my_dict["Age"])
print(my_dict.get("Class"))
print(my_dict.values())

for x in my_dict:
    print(my_dict[x])

for x,y in my_dict.items():
    print(x,y)

my_dict ["IT"] = "Meta physics"
print(my_dict)

my_dict ["Color"] = "Red"
print(my_dict)
my_dict.popitem()
print(my_dict)

del my_dict ["Age"]
print(my_dict)