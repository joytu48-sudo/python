print("Enter your choice of travelling:")
print("1|Car")
print("2|Bike")
choice = int(input("Enter 1 or 2: "))

if choice == 1:
    print("What model do your want?:")
    print("Toyota Premio")
    print("Hiace")
    choice2 = int(input("Enter 1 or 2: "))
    
    if choice2 == 1:
        print("You picked toyota Premio")
    else:
        print("You picked Hiace")

elif choice == 2:
    print("What model do you want?:")
    print("Motorbike")
    print("Scooter")
    choice2 = int(input("Enter 1 or 2: "))

    if choice2 == 1:
        print("You have picked motorbike")
    else:
        print("You have picked scooter")

else:
    print("Invalid number. plese choose the option given")