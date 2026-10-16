student = {
    "Name": "Sushmoy",
    "Age": 13,
    "School": "Mastermind English Medium School",
}

print(student)

#Length
print("Length", len(student))

#Add
student["Country"] = "Bangladesh"
print(student)

#update
student["Age"] = 14
print(student)

#loop
for item in student:
    print(student[item])

#delete an item
student.pop("Country")
print(student)

#clear
student.clear()
print(student)