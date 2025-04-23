from beverage import Beverage

class HouseBlend(Beverage):
    def get_description(self) -> str:
        return "House Blend Coffee"

    def get_cost(self) -> float:
        return 0.99