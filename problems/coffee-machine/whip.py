from condiment_decorator import CondimentDecorator

class Whip(CondimentDecorator):
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def get_cost(self) -> float:
        return self.beverage.get_cost() + .30