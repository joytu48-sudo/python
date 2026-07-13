x = 32
y = 7.8789
name = "sushmoy"
isStudent = True

#Type of data
print(type(x))
print(type(y))
print(type(name))
print(type(isStudent))
#typecasting
y = int(y)
print(f"The value of y after typecasting is:{y}.\nThe data type of y is{type(y)}")
x = float(x)
print(f"The value of x after typecasting is:{x}.\nThe data type of x is{type(x)}")

word1 = input("enter your word:")

#indexing
print(f"first charecter is:{word1[0]}")
print(f"last charecter is:{word1[-1]}")
#slicing
print(f"after slicing:{word1[0:4]}")
#Concatenation
word2 = " is a coder"
word3 = word1+word2
print(word3)
#reversing
print(f"after reversing:{word1[::-1]}")