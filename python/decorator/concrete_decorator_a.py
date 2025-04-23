from decorator import Decorator

class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self):
        return f"ConcreteDecoratorA operation({self.component.operation()})"