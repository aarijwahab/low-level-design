from machine_state import MachineState
from cash import Cash
from coin import Coin
from product import Product
from inventory import Inventory

class GiveChangeState(MachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def selectProduct(self, product: Product):
        print("Please collect the change first")

    def insertCoin(self, coin: Coin):
        print("Please collect the change first")

    def insertCash(self, cash: Cash):
        print("Please collect the change first")

    def dispenseProduct(self):
        print("Please collect the change first")

    def giveChange(self):
        change = self.vending_machine.money_inserted - self.vending_machine.selected_product.getPrice()
        if change > 0:
            print(f"Change returned: ${change:.2f}")
            self.vending_machine.resetPayment()
        else:
            print("No change to return.")
        self.vending_machine.resetProduct()
        self.vending_machine.setState(self.vending_machine.idle_state)