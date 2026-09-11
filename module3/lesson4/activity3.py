valid = False
while not valid:
    try:
        n = int(input("Enter: "))
        while n%2 == 0:
            print("BYE")
            valid = True
    except ValueError as ex:
        print(ex)