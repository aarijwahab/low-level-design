from condiment_decorator import CondimentDecorator

class Mocha(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def get_cost(self) -> float:
        return self.beverage.get_cost() + .50