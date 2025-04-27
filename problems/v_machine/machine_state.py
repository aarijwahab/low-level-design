from abc import ABC, abstractmethod
from product import Product
from coin import Coin
from cash import Cash

class MachineState(ABC):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    @abstractmethod
    def selectProduct(self, product: Product):
        pass

    @abstractmethod
    def insertCoin(self, coin: Coin):
        pass

    @abstractmethod
    def insertCash(self, cash: Cash):
        pass

    @abstractmethod
    def dispenseProduct(self):
        pass

    @abstractmethod
    def giveChange(self):
        pass