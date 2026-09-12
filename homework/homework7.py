valid = False
while not valid:
    try:
        people = int(input("Enter: ")) 
        if people <= 0:
            print("number is not valid")
    except ValueError as ex:
        print(ex)
        break
    else:
            try:
                bill_amount = float(input("Enter amount: "))
                if bill_amount <= 0:
                    print("bill amount is not valid, please try again")
            except ValueError as ex:
                print(ex)
                break
            else:
                    try:
                        original_price = float(input("Enter original price: "))

                        if original_price <= 0:
                            print("Original price must be positive.")
                            break
                        else:
                            final_price = float(input("Enter final price after discount: "))
                        if final_price > original_price:
                                print("Final price cannot be higher than original price.")
                                break
                        else:
                            discount_amount = original_price - final_price
                            discount_percentage = (discount_amount / original_price) * 100
                            if discount_percentage <= 0:
                                print("invalid discount")
                    except ValueError as ex:
                            print(ex)
                            break
                    else:
                        print(discount_percentage)

                                        