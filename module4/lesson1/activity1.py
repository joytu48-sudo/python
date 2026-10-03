List = [223,231.23,"Tasmia",False,"True"]

#how many items
print("Length of the list i made => ",len(List))

#accessing through index
print(List[3-1])
print(List[0])
print(List[-1])#last

#taking a portion from the list
print("slicing -) ",List[2:4])

#through loop
for l in List:
    print(l)

#multiply
print(List*3)

List = List[::-1]
print("|Reversed|",List)