class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    
    def create_cheese_burger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def create_deluxe_cheese_burger(self):
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)

    def create_vegan_burger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)

if __name__ == "__main__":
    burgerFactory = BurgerFactory()
    burgerFactory.create_cheese_burger().print()
    burgerFactory.create_deluxe_cheese_burger().print()
    burgerFactory.create_vegan_burger().print()
