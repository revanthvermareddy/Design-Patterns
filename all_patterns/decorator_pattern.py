"""
Description:
    The Decorator pattern allows you to add behavior to objects dynamically.

Explanation: 
    The ToyFactory creates toys based on the type you provide.
    You don't need to know the specific class of the toy; just ask the factory for what you want, and it will give you the correct object.
    It's like telling a toy factory, “I want a car,” and it handles the rest.
"""

class Toy:
    def cost(self):
        return 10

class ToyWithGiftWrap:
    def __init__(self, toy):
        self._toy = toy

    def cost(self):
        return self._toy.cost() + 5

class ToyWithBatteries:
    def __init__(self, toy):
        self._toy = toy

    def cost(self):
        return self._toy.cost() + 2

# Usage
basic_toy = Toy()
wrapped_toy = ToyWithGiftWrap(basic_toy)
wrapped_toy_with_batteries = ToyWithBatteries(wrapped_toy)

print(wrapped_toy_with_batteries.cost())  # Output: 17