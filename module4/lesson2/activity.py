tuple = (34,231.23,"Coding", False)

#Length of the tuple(how many items there are)
print("Length of tuple ", len(tuple))

#Aceess items with index
print(tuple[2])
print(tuple[0])#first
print(tuple[-1])#last

#slicing
print(tuple[1:3])

#Add new items to tuple
tuple = tuple + (34,)
print(tuple)

#count number of same items
print("no. of 34 ",tuple.count(34))