class parent:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height
    def show_details(self):
        print("eye color ",self.eye_color)
        print("height ",self.height)

class child(parent):
    def __init__(self,name, age, eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)

    def show_details(self):
        print("name ",self.name)
        print("age ",self.age)
        super().show_details()

    def fav_hobby(self, hobby):
        print(self.name,"loves",hobby)

kid = child("Sushmoy",13,"brown","173")
kid.show_details()
kid.fav_hobby("art")

print("Am i the subclass of my parent? ",issubclass(child,parent))