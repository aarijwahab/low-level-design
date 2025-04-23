from beverage import Beverage
from mocha import Mocha
from whip import Whip
from house_blend import HouseBlend

class CoffeeBuilder:
    def __init__(self):
        self.beverage = None
    
    def use_house_blend(self):
        self.beverage = HouseBlend()
        return self
    
    def add_mocha(self):
        self.beverage = Mocha(self.beverage)
        return self
    
    def add_whip(self):
        self.beverage = Whip(self.beverage)
        return self

    def build(self) -> Beverage:
        return self.beverage