class computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"selling price {self.__maxprice}")

    def newprice(self, price):
        self.__maxprice = price

Cobj = computer()
Cobj.sell()

#no attribute
Cobj.__maxprice = 1200
Cobj.sell()

Cobj.newprice(1200)
Cobj.sell()