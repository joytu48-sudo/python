total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customer_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Please enter your name: ")
    amount = int(input(f"Hello {name}, please enter your withdrawal amount."))

    if amount <= 0:
        print("amount is invalid, please enter a valid amount.")
        continue
    print(f"dispensing {amount} bdt for {name}")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1:
            value = 100
        elif idx == 2:
            value = 50
        elif idx == 3:
            value = 20
        elif idx == 4:
            value = 10
        elif idx == 5:
            value = 5
        else:
            value = 1

        count = remaining // value 

        if count > 0:
            print(f"{count}X{value} = {count*value} BDT")
            remaining -= count*value
            if value == 100:
                total_100 += 100
            elif value == 50:
                    total_50 += 50
            elif value == 20:
                        total_20 += 20
            elif value == 10:
                        total_10 += 10
            elif value == 5:
                        total_5 += 5
            elif value == 1:
                        total_1 += 1

        idx += 1

    customer_served += 1
    total_dispensed += amount
    again = input("Would you like to serve another customer? ( yes | no )").lower()
    if again == "no":
          serving = False