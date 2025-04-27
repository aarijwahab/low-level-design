from product import Product
from inventory import Inventory
from idle_state import IdleState
from give_change_state import GiveChangeState
from dispense_state import DispenseState
from interaction_state import InteractionState
from machine_state import MachineState
from coin import Coin
from cash import Cash

class TheVendingMachine:
    def __init__(self):
        self.money_inserted = 0.0
        self.selected_product = None
        self.inventory = Inventory()
        self.idle_state = IdleState(self)
        self.dispense_state = DispenseState(self)
        self.give_change_state = GiveChangeState(self)
        self.interaction_state = InteractionState(self)
        self.current_state = self.idle_state
    
    def setState(self, state: MachineState):
        self.current_state = state
    
    def addCoin(self, coin: Coin):
        self.money_inserted += coin.value
    
    def addCash(self, cash: Cash):
        self.money_inserted += cash.value
    
    def resetPayment(self):
        self.money_inserted = 0.0
    
    def resetProduct(self):
        self.selected_product = None

    def selectProduct(self, product: Product):
        self.current_state.selectProduct(product)

    def insertCoin(self, coin: Coin):
        self.current_state.insertCoin(coin)

    def insertCash(self, cash: Cash):
        self.current_state.insertCash(cash)

    def dispenseProduct(self):
        self.current_state.dispenseProduct()

    def giveChange(self):
        self.current_state.giveChange()