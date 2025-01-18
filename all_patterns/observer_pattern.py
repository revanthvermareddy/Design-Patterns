"""
Description:
    The Observer pattern allows an object (the subject) to notify other objects (observers) when its state changes.

Explanation: 
    The ToyStore can notify all Customer objects when a new toy arrives.
    Each customer automatically gets the news without constantly checking the store.
    It's like being on a mailing list where you get an alert whenever something new is available.
"""


class ToyStore:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, toy):
        for observer in self._observers:
            observer.update(toy)

    def new_toy_arrival(self, toy):
        print(f"New toy arrived: {toy}")
        self.notify_observers(toy)

class Customer:
    def update(self, toy):
        print(f"Customer is notified: {toy} is now available!")

# Usage
store = ToyStore()
customer = Customer()
store.add_observer(customer)

store.new_toy_arrival("RC Car")  
# Output:
# New toy arrived: RC Car
# Customer is notified: RC Car is now available!