class Product():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def getPrice(self):
        return self.__price
    
    def getName(self):
        return self.__name
