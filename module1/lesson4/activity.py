field1 = 150
field2 = 85
field3 = 120
field4 = 95
field5 = 115

total = field1 + field2 + field3 + field4 + field5
avg = total/5
print(f"total harvest:{total}")
print(f"average per field:{avg}")

price_per_KG = 15
earnings = total*price_per_KG
print(f"total earnings is:{earnings}bdt")

bags = total//25
leftover = total%25
print(f"full bags packed:{bags}")
print(f"leftovers:{leftover}")

last_year = 500
print(f"better then last year?:{total > last_year}")
print(f"same as last year?:{total == last_year}")
print(f"at least same as last year?:{total >= last_year}")

total += 30
print(f"after bonus crop:{total}kg")

total -= 15
print(f"after seed reserve:{total}kg")

bags = total//25
print(f"final bags packed:{bags}")