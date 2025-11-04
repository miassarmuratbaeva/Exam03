class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is driving"
vehicle1 = Vehicle("kawasaki 250 ", "Ducasu ")
car1 = Car("Toyota", "Corolla")
print(vehicle1.move()) 
print(car1.move())