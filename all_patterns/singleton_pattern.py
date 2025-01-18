"""
Description:
    The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

Explanation: 
    Here, ToyStore is a Singleton class.
    No matter how many times you try to create a ToyStore object, you'll always get the same instance.
    This is like having only one toy store in the whole town - no duplicates.
"""


class ToyStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ToyStore, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

# Usage
store1 = ToyStore()
store2 = ToyStore()

store1.add_toy("Action Figure")
print(store2.toys)  # Output: ['Action Figure']