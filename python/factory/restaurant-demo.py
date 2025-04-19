from veggie_burger_restaurant import VeggieBurgerRestaurant
from beef_burger_restaurant import BeefBurgerRestaurant
from restaurant import Restaurant

class RestaurantDemo:

    def run(sef):
        veggie_restaurant: Restaurant = VeggieBurgerRestaurant()
        beef_restaurant: Restaurant = BeefBurgerRestaurant()

        beef_restaurant.orderBurger()
        veggie_restaurant.orderBurger()
    
if __name__ == "__main__":
    resDemo = RestaurantDemo()
    resDemo.run()