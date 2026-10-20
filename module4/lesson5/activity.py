necessity = ["chupa chups", "Pencil", "Mechanical pencil", "ballpoint pen", "Gel pen", "Bag of chips"]
stock_count = [0, 23, 9, 10, 0, 13]

inventory = {item: count for item, count in zip(necessity, stock_count)}
print("Items available: ", inventory)

in_stock = [item for item in necessity if inventory[item]>0]
print("items in stock: ",in_stock)

chosen_item = input("Which one you buy?>")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"{chosen_item} out of stock, bad luck, chose another one")

price = [23,21,23,35,5,3]
price_with_vat =list(map(lambda price: price + 10, price))
print("Price with vat: ", price_with_vat)