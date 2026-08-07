rowSize = int(input("Enter your number: "))

if rowSize % 2 == 0:
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2) + 1

for i in range (1, halfDiamRow +1):
    spaces = " "* (halfDiamRow - i)
    numbers = "".join(str(num) for num in range(1,2*i))
    print(spaces + numbers) 

for i in range (1, halfDiamRow):
    spaces = " "* i
    numbers = "".join(str(num) for num in range(1,2* (halfDiamRow - i)))
    print(spaces + numbers)

