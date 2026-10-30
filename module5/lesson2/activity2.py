class Employee:
    #constructor
    def __init__(self):
        print("Employee created")

    #destructor
    def __del__(self):
        print("destructor called")

def create_obj():
    print("making an object")
    obj = Employee()
    print("function ends")
    return obj
print("Calling create_obj() function")
obj = create_obj()
print("program end")

        