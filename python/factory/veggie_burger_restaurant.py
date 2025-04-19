from restaurant import Restaurant
from veggie_burger import VeggieBurger 

class VeggieBurgerRestaurant(Restaurant):

    def createBurger(self):
        return VeggieBurger()