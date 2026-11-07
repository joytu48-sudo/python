from abc import ABC, abstractmethod

#base class
class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("i have hands")

class giraffe(animal):
    def move(self):
        print("I have a long neck")

class cow(animal):
    def move(self):
        print("i can moo")

class wolf(animal):
    def move(self):
        print("i can woof")

h = human()
h.move()

g = giraffe()
g.move()

c = cow()
c.move()

w = wolf()
w.move()