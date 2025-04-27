from vending_machine_class import TheVendingMachine
from product import Product
from coin import Coin
from cash import Cash

class TheVendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = TheVendingMachine()

        # Add products to the inventory
        coke = Product("Coke", 1.5)
        pepsi = Product("Pepsi", 1.5)
        water = Product("Water", 1.0)

        vending_machine.inventory.addProduct(coke, 5)
        vending_machine.inventory.addProduct(pepsi, 3)
        vending_machine.inventory.addProduct(water, 2)

        # Select a product
        vending_machine.selectProduct(coke)

        # Insert coins
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)

        # Insert a cash
        vending_machine.insertCash(Cash.FIVE)

        # Dispense the product
        vending_machine.dispenseProduct()

        # Return change
        vending_machine.giveChange()

        # Select another product
        vending_machine.selectProduct(pepsi)

        # Insert insufficient payment
        vending_machine.insertCoin(Coin.QUARTER)

        # Try to dispense the product
        vending_machine.dispenseProduct()

        # Insert more coins
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)
        vending_machine.insertCoin(Coin.QUARTER)

        # Dispense the product
        vending_machine.dispenseProduct()

        # Return change
        vending_machine.giveChange()

if __name__ == "__main__":
    TheVendingMachineDemo.run()