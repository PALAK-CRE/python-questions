print("Question 1")
print("Answer")

info = {
    "name": "Kadambini Yadav",
    "age": 18,
    "gender": "Female"
}

print(info)


print("\nQuestion 2")
print("Answer")

info = {
    "name": "Kadambini Yadav",
    "age": 18,
    "gender": "Female"
}

print(info["name"])


print("\nQuestion 3")
print("Answer")

info = {
    "name": "Kadambini Yadav",
    "age": 18,
    "gender": "Female"
}

print(list(info.values()))


print("\nQuestion 4")
print("Answer")

info = {
    "name": "Kadambini Yadav",
    "age": 18,
    "gender": "Female"
}

info["age"] = 19
print(info)


print("\nQuestion 5")
print("Answer")

info = {
    "name": "Kadambini Yadav",
    "age": 18,
    "gender": "Female"
}

for key in info:
    print(key)


print("\nQuestion 6")
print("Answer")

student = {
    "student1": {"name": "Aman", "age": 18},
    "student2": {"name": "Riya", "age": 19},
    "student3": {"name": "Kadambini", "age": 18}
}

print(student)


print("\nQuestion 7")
print("Answer")

d1 = {"name": "Kadambini"}
d2 = {"age": 18}
d3 = {"gender": "Female"}

combined = {
    "dict1": d1,
    "dict2": d2,
    "dict3": d3
}

print(combined)


print("\nQuestion 8")
print("Answer")

list1 = ["name", "age", "gender"]
list2 = ["Kadambini", 18, "Female"]

result = dict(zip(list1, list2))
print(result)


print("\nQuestion 9")
print("Answer")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)


print("\nQuestion 10")
print("Answer")

marks = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

print(min(marks, key=marks.get))