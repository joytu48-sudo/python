class vehicle:
    #constructor
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = vehicle(230, 18)
print(f"The car model has max speed of {car.max_speed} and mileage of {car.mileage}")