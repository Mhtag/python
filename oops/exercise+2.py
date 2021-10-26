class Vehicle:
    color = 'White'
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def __str__(self):
        return f"Color: {self.color} Name: {self.name} Mileage: {self.mileage} Max Speed: {self.max_speed}"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

class Car(Vehicle):
    pass




school_bus = Bus('TATA', 5, 80)

car = Car('AudiQ5', 10, 180)


print(school_bus)