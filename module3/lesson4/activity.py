try:
    number = int(input("Enter your number: "))
    print("The number you entered was ")
except ValueError:
    print("Your number must be an integer number")