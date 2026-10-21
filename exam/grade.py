Grade = {"Arhaan": 21,
         "Sushmoy":98,
         "Subham":96,}

total = 0
for score in Grade.values():
    total += score

average = total / len(Grade)
print(average)

topper = max(Grade, key=Grade.get)
bottomer = min(Grade, key=Grade.get)

print(topper)
print(bottomer)

search = input("Enter name:")

student_grade = Grade.get(search)

if student_grade is not None:
    print(f"{search},{student_grade}")
else:
    print("unavailable")