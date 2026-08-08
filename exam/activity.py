import random
unknown = random.randint(1, 100)
attempts = 0

while True:
    number = int(input("Guess your number: "))
    attempts -= 1

    if number <= unknown:
        print("The unknown is cold")
    elif number >= unknown:
        print("The unknown is hot")
    else:
        print(f"The unknown is discovered to be {unknown}")