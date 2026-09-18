

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "error"
    return a / b
    

def calculator():
    while True:
        print("Select your options: ")
        print("1) add")
        print("2) subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) leave")

    choice = input("Enter: ")

    if choice == "5":
        print("leaves")
        break
    if choice == "1", "2", "3", "4"
        try:
            a = input("Enter: ")
            b = input("Enter: ")
        except ValueError:
            print("number please")
            continue

    if choice == "1":
        print(f'result: {a} + {b} = {add(a, b)}')
    elif choice == "2":
            print(f'result: {a} - {b} = {sub(a, b)}')
    elif choice == "3":
            print(f'result: {a} * {b} = {multiply(a, b)}')
    elif choice == "4":
            print(f'result: {a} / {b} = {divide(a, b)}')
    else:
         print("invalid")



