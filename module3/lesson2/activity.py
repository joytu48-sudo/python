def total_bill(bill_amount, tip_perc):
    """This function finds out total payable amount"""
    total = bill_amount * (1 + 0.01 * tip_perc)
    return total

print(total_bill.__doc__)
print(total_bill(415,15))