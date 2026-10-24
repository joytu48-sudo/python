class IOstring:
    #constructor
    def __init__(self):
        self.str1 = ""

        #m1
    def get_str(self):
            self.str1 = input("Enter word: ")

        #m2
    def print_str(self):
            print("Result: ",self.str1.upper())

obj = IOstring()
obj.get_str()
obj.print_str()