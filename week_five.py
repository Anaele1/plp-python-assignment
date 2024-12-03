

#Activity 2

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bike(Vehicle):
    def move(self):
        print("Cycling 🚴")

class Train(Vehicle):
    def move(self):
        print("Chugging along 🚂")

class Ship(Vehicle):
    def move(self):
        print("Sailing 🛳️")

class Truck(Vehicle):
    def move(self):
        print("Trucking along 🚚")

class Motorcycle(Vehicle):
    def move(self):
        print("Riding 🏍️")

class Helicopter(Vehicle):
    def move(self):
        print("Flying rotor 🚁")

class Boat(Vehicle):
    def move(self):
        print("Sailing boat 🛥️")

class Animal(Vehicle):
    def move(self):
        print("Running 🐾")


car = Car()
plane = Plane()
bike = Bike()
train = Train()
ship = Ship()
truck = Truck()
motorcycle = Motorcycle()
helicopter = Helicopter()
boat = Boat()
animal = Animal()

Call move() method
print("Vehicles in motion:")
car.move()
plane.move()
bike.move()
train.move()
ship.move()
truck.move()
motorcycle.move()
helicopter.move()
boat.move()
animal.move()
