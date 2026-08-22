def cube(number):
    return number**3

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

number = int(input("Enter your number: "))
print(by_three(number))
