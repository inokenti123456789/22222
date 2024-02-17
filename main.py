class Car:
    wheels = 4
    doors = 4
    fuel_type = "petrol"

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

    def honk(self):
        print("Beep beep!")


class Dog:
    legs = 4
    tail = True
    sound = "bark"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def eat(self):
        print(f"{self.name} is eating.")

car1 = Car("Toyota", "Corolla", "blue")
car2 = Car("Honda", "Civic", "red")
car3 = Car("Ford", "Fusion", "silver")

dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Labrador", 2)
dog3 = Dog("Bella", "Poodle", 5)