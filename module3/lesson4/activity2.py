try:
    num1, num2 = eval(input("Enter your number separated by a comma: "))
    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Divided by 0 is not possible")

except SyntaxError:
    print("There must be a comma")

except ValueError:
    print("Must be a number")

else:
    print("no excpetions")

finally:
    print("code will run no matter what")