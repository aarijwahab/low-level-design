class Product1():

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def listParts(self):
        print(f"Product parts: {self.parts}")
    