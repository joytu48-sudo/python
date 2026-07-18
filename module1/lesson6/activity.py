print("Answer these 3 question to start your planning:")

day = input("What day is today?(monday-sunday): ").lower()
weather = input("How is the weather outside?(sunny|rainy|cloudy): ").lower()
homework = input("Is your homework done?(yes|no): ").lower()

if day in ("saturday,sunday"):
    print("It's the weekend, enjoy your freetime!")
elif day == "monday":
    print("First day of the week, goodluck!")
elif day in ("tuesday, wednesday, thursday"):
    print("Regular day at school, stay focused!")
elif day == "friday":
    print("Last day at school! please return your library books")
else:
    print("Day is not recognised, please check your spelling")

if weather == "sunny" and homework == "yes":
    print("Have a great day playing outside!")
elif weather == "rainy" or weather == "cloudy":
    print("Better sat at home and do your homework")
elif weather == "rainy" and not homework == "yes":
    print("you should stay inside and do your homework")
elif weather == "sunny" and homework == "yes" and day not in ("saturday, sunday"):
    print("Have a great sunny day outside!")
print("have a great day")