from product import Product

class Inventory:
    def __init__(self):
        self.products = {}
    
    def addProduct(self, product, quantity):
        self.products[product] = quantity
    
    def deleteProduct(self, product):
        del self.products[product]
    
    def updateQuantity(self, product, quantity):
        self.products[product] = quantity
    
    def getQuantity(self, product):
        return self.products[product]
    
    def isAvailable(self, product):
        return product in self.products and self.products[product] > 0
    
    def decrementQuantity(self, product):
        if product in self.products and self.products[product] > 0:
            self.products[product] -= 1