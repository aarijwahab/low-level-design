from abc import ABC, abstractmethod
from burger import Burger

# This is our Restaurant Factory Class. It is extended by other restaurants
class Restaurant(ABC):
    @abstractmethod
    def createBurger(self):
        pass

    def orderBurger(self) -> Burger:
        burger: Burger = self.createBurger()
        burger.prepare()
        return burger

