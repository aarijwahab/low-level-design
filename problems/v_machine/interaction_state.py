from machine_state import MachineState
from cash import Cash
from coin import Coin
from product import Product

"""
Here they can insert money or ask for their change back
"""
class InteractionState(MachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def selectProduct(self, product: Product):
        print("Product already selected")

    def insertCoin(self, coin: Coin):
        self.vending_machine.addCoin(coin)
        print(f"Coin inserted: {coin.name}")
        print(f"Current total: {self.vending_machine.money_inserted}")
        self.checkPaymentStatus()

    def insertCash(self, cash: Cash):
        self.vending_machine.addCoin(cash)
        print(f"Cash inserted: {cash.name}")
        print(f"Current total: {self.vending_machine.money_inserted}")
        self.checkPaymentStatus()

    def dispenseProduct(self):
        print("Not enough money has been inserted yet")

    def giveChange(self):
        change = self.vending_machine.money_inserted - self.vending_machine.selected_product.getPrice()
        if change > 0:
            print(f"Change returned: ${change:.2f}")
            self.vending_machine.resetPayment()
        else:
            print("No change to return")
        self.vending_machine.setState(self.vending_machine.idle_state)

    def checkPaymentStatus(self):
        if self.vending_machine.money_inserted >= self.vending_machine.selected_product.getPrice():
            self.vending_machine.setState(self.vending_machine.dispense_state)