class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__(self):
        return f"This is a {self.color} car with {self.mileage:,} miles."
    def drive(self, mile):
        self.mileage = mile
        return self.mileage
blue_car = Car("Blue",20000)
red_car = Car("Red",30000)
print(blue_car)
print(f"The {blue_car.color} car has {blue_car.mileage:,} miles.")
print(f"The {red_car.color} car has {red_car.mileage:,} miles.")
new_car = Car("Yellow",0)
print(f"The new {new_car.color} car has {new_car.mileage} miles.")
new_car.drive(100)
print(f"The new {new_car.color} car has now driven {new_car.mileage} miles.")