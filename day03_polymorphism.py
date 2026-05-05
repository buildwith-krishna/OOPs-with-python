class Vehicle:
    def move(self):
        print("Vehicle is moving!")

class Car(Vehicle):
    def move(self):
        print("Car is being driven on the road.")

class Boat(Vehicle):
    def move(self):
        print("Boat is being sailed in the river.")

class Plane(Vehicle):
    def move(self):
        print("plane is flying in the sky")

vehicles = [Vehicle(), Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()
