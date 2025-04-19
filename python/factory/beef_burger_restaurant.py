from restaurant import Restaurant
from beef_burger import BeefBurger

class BeefBurgerRestaurant(Restaurant):
    def createBurger(self):
        return BeefBurger()