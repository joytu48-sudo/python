print("Welcome to the holiday planner where we help you decide how to spent your holiday!\nWhat type of holiday are you looking for?:")
print("1|Beach holiday")
print("2|Mountain holiday")
choice = int(input("Enter 1 or 2: "))

if choice == 1:
    print("Looking to chill out by the sun i see!\nWhat activity would you like to do out in the hot sandy area?:")
    print("Build a sandcastle")
    print("Go out for a swim")
    choice2 = int(input("Enter 1 or 2: "))
    
    if choice2 == 1:
        print("-You decided to build a sand castle-")
        print("🛕")
    else:
        print("-You decided to swim out with the blissful waves of the glistening sea-")
        print("♒︎♒︎♒︎♒︎♒︎")

elif choice == 2:
    print("quite adventurous!\n what activity would you like to do brave hero?:")
    print("hike")
    print("camp")
    choice2 = int(input("Enter 1 or 2: "))

    if choice2 == 1:
        print("-you decided to hike through the treacherous vegetation of mother nature's home-")
        print("⛰︎ ོ ༄ 𓀙")
    else:
        print("-you decided to camp with the vegetation of mother nature")
        print("⛺")


else:
    print("Invalid number. plese choose the option given")