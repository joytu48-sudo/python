#return - returns the result backto func.
def add(a,b):
    return a+b
print(add(5,10))

#break - if the condition is true, it simply breaks the loop
for i in range(1,11):
    if i%2 !=0:
        print(f"odd no. has been found: {i}")
    else:
        print("even no. has been found, we'll sbreak the loop for now")
        break

#continue - if conditions are met, it skips the value
for i in range(1,11):
    if i%2 !=0:
        print(f"odd no. has been found: {i}")
    else:
        continue

#pass - does nothing, used to avoid errors when no value has been given

bill_amount = int(input("Enter your bill amount please: "))
paid_amount = int(input("Enter your paid amount please: "))
change = bill_amount - paid_amount

if change == 0:
    pass
else:
    print(change)