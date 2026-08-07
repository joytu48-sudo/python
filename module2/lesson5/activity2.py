num_of_rows = int(input("Enter your number: "))
number = 1

for i in range(num_of_rows):
    for j in range(i+1):
        print(number, end=" ")
        number += 1
    print()