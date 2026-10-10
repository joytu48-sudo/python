Tuple_Weather = (1,0,0,0,1,1,0)

Rainy = 0
Sunny = 0

for i in range(0,7):
    if Tuple_Weather[i] == 1:
        Rainy += 1
    else:
        Sunny += 1

if Rainy > Sunny:
    print("Baire bristi hobe, chata ene baire jao")
else:
    print("Baire rod ashbe, sunscreen meghe baire jao")
