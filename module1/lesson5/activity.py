temperature = int(input("Enter the temperature in celcius: "))
if temperature < 20:
    outfit = "jacket"
    print(f"The weather is cold today, please wear a {outfit}")
else:
    outfit = "t-shirt"
    print(f"The weather is hot today, please wear a {outfit}")

is_raining = input("Is it raining outside?(yes|no): ")
if is_raining == "yes":
    print("bring your umbrella when going out")
else:
    print("no need for your umbrella when going out")

wind_speed = int(input("How strong is the wind today? Answer in km/h: "))
if wind_speed > 30:
    needs_windbreaker = "yes"
    print(f"It is very windy outside, please wear your windbreaker over your {outfit}")
else:
    needs_windbreaker = "no"
    print(f"Theres no wind outside, no need to wear a windbreaker on your {outfit}")

has_puddles = input("Is there any puddles outside?(yes|no): ")
if has_puddles == "yes":
    shoes = "boots"
    print(f"Wear {shoes} when going outside")
else:
    shoes = "sneakers"
    print(f"wear {shoes} when going outside")

print("\nThe weather check is complete")

print("temperature: ",temperature)
print("outfit chosen: ",outfit)
print("is raining outside: ",is_raining)
print("need windbreaker?: ",needs_windbreaker)
print("has puddles outside?: ",has_puddles)