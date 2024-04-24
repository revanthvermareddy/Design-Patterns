from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def remove_value(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def remove_value(self, val):
        return val < 0 

class RemoveOddStrategy(FilterStrategy):

    def remove_value(self, val):
        return abs(val) % 2


class Values:
    def __init__(self, vals):
        self.vals = vals
    
    def filter(self, strategy):
        res = []
        for n in self.vals:
            if not strategy.remove_value(n):
                res.append(n)
        return res


if __name__ == "__main__":
    initial = [-7, -4, -1, 0, 2, 6, 9]
    values = Values(initial)

    print('inital:', initial)
    print('after remove negative:', values.filter(RemoveNegativeStrategy()))
    print('after remove odd:', values.filter(RemoveOddStrategy()))
