# Assignment 1

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_borrowed = False

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: ${self.price:.2f}")
        print(f"Borrowed: {'Yes' if self.is_borrowed else 'No'}")

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'")
        else:
            print(f"'{self.title}' is not borrowed")
class EBook(Book):
    def __init__(self, title, author, pages, price, file_size):
        super().__init__(title, author, pages, price)
        self.file_size = file_size

    def display_details(self):
        super().display_details()
        print(f"File Size: {self.file_size} MB")


class Audiobook(Book):
    def __init__(self, title, author, pages, price, duration):
        super().__init__(title, author, pages, price)
        self.duration = duration

    def display_details(self):
        super().display_details()
        print(f"Duration: {self.duration} hours")


book1 = Book("To Kill a Mockingbird", "Harper Lee", 281, 15.99)
ebook1 = EBook("1984", "George Orwell", 328, 9.99, 2.5)
audiobook1 = Audiobook("The Great Gatsby", "F. Scott Fitzgerald", 180, 14.99, 6.5)


book1.display_details()
book1.borrow_book()
book1.return_book()

ebook1.display_details()
ebook1.borrow_book()
ebook1.return_book()

audiobook1.display_details()
audiobook1.borrow_book()
audiobook1.return_book()

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
