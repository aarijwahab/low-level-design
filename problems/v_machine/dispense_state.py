from machine_state import MachineState
from cash import Cash
from coin import Coin
from product import Product


class DispenseState(MachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def selectProduct(self, product: Product):
        print("Product already selected. Please collect the dispensed product.")

    def insertCoin(self, coin: Coin):
        print("Payment already made. Please collect the dispensed product.")

    def insertCash(self, cash: Cash):
        print("Payment already made. Please collect the dispensed product.")

    def dispenseProduct(self):
        product: Product = self.vending_machine.selected_product
        self.vending_machine.inventory.decrementQuantity(product)
        print(f"Product dispensed: {product.getName()}")
        self.vending_machine.setState(self.vending_machine.give_change_state)

    def giveChange(self):
        print("Please collect the dispensed product.")