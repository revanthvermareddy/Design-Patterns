"""
Description:
    The Factory pattern provides a way to create objects without specifying the exact class of the object that will be created.

Explanation: 
    The ToyFactory creates toys based on the type you provide.
    You don't need to know the specific class of the toy; just ask the factory for what you want, and it will give you the correct object.
    It's like telling a toy factory, “I want a car,” and it handles the rest.
"""


class Toy:
    def play(self):
        pass

class Car(Toy):
    def play(self):
        return "Vroom!"

class Doll(Toy):
    def play(self):
        return "I'm a doll!"

class ToyFactory:
    @staticmethod
    def create_toy(toy_type):
        if toy_type == "Car":
            return Car()
        elif toy_type == "Doll":
            return Doll()
        else:
            raise ValueError("Unknown toy type")

# Usage
toy = ToyFactory.create_toy("Car")
print(toy.play())  # Output: 'Vroom!'