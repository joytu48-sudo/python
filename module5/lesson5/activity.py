from abc import ABC, abstractmethod

#Base class
class absClass(ABC):
    #Function
    def print(self, x):
        print("Value ",x)

    #Abstract method
    @abstractmethod
    def task(self):
        print("Im a abstract method")

class test_class(absClass):
    def task(self):
        print("We're inside the subclass")

obj = test_class()
obj.task()
obj.print(6489)