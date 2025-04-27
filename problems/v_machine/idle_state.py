from machine_state import MachineState
from cash import Cash
from coin import Coin
from product import Product

class IdleState(MachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def selectProduct(self, product: Product):
        if self.vending_machine.inventory.isAvailable(product):
            self.vending_machine.selected_product = product
            self.vending_machine.setState(self.vending_machine.interaction_state)
            print(f"Product selected: {product.getName()}")
        else:
            print(f"Product not available: {product.getName()}")

    def insertCoin(self, coin: Coin):
        print("Select a product first")

    def insertCash(self, cash: Cash):
        print("Select a product first")

    def dispenseProduct(self):
        print("Select a product first")

    def giveChange(self):
        print("Select a product first")