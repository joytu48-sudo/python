Dictionary = {
    "Codingal":2,
    "is":2,
    "good enough":1,
}

print("Original",Dictionary)

value = 2

count = 0

for key in Dictionary:
    if Dictionary[key] == value:
        count += 1

print("Frequency is",count)
