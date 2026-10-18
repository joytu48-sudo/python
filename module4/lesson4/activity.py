fruits = {"Mango","Lychee","Watermelon","Apple",'Guava'}
print(fruits)

#add new items
fruits.add("Pear")
print(fruits)

#interseption1
fruits2 = {"Watermelon","Pineapple","Jackfruit","Pear"}
print("interseption: ",fruits.intersection(fruits2))

#intersection2
common = fruits.intersection(fruits2)
print("intersection2: ",common)

import array as ar
fruits_count = ar.array("i",[1,8,92,3,2,90,2,3,1,2,8])
print("Fruit count as array; ",fruits_count)

#add new items
fruits_count.insert(0,7)
print(fruits_count)

#add with position
fruits_count.append(10)
print(fruits_count)

#count the repitation
print("number of repitation of the number 2: ",fruits_count.count(2))

#reverse
fruits_count.reverse()
print(fruits_count)