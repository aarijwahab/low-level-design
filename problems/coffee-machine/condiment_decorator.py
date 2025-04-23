from beverage import Beverage
class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description()

    def get_cost(self) -> float:
        return self.beverage.get_cost()