def greet_customer():
    print("Welcome to the lemonade stand!")
    print("Fresh lemonade, made just for you")

greet_customer()

price_per_cup = float(input("Enter your price per cup in dollar: "))
cups_sold = int(input("Enter the number of cup sold: "))

def calculate_total(price_per_cup, cups_sold):
    total = price_per_cup * cups_sold
    return total
total_cost = calculate_total(price_per_cup, cups_sold)
print("Total cost: ", total_cost)

ammount_paid = float(input("Enter the ammount paid by the customer: "))

def calculate_change(ammount_paid, total_cost):
    change = ammount_paid - total_cost
    return change

change_due = calculate_change(ammount_paid, total_cost)
print("Total change", change_due)

def thank_you_msg(cups_sold):
    if cups_sold >= 5:
        return 'Wow, a big order! thank you so much!'
    else:
        return "thaanks for stopping by!"

closing_message = thank_you_msg(cups_sold)
print(closing_message)