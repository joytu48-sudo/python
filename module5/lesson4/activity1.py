class myClass:
#private variable
    __privateVar = 78
#private method
    def __privMeth(self):
        print("Im a private method")

#Public method
    def hello(self):
        print("Private variable ",myClass.__privateVar)

obj = myClass()
obj.hello()
obj.__privMeth()