import random

playing = True
num = str(random.randint(1,10))

print("Your system has chosen a number, please guess the number")

while playing:
    guess = input("Enter your guess")
    if num == guess:
        print("you are correct!Answer", num)
        break
    else:
        print("wrong, try again")
