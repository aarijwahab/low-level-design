from decorator import Decorator

class ConcreteDecoratorB(Decorator):
    """
    Decorators may call parent implementation of the operation, instead of
    calling the wrapped object directly. This approach simplifies extension
    of decorator classes.
    """

    def operation(self):
        return f"ConcreteDecoratorB operation({self.component.operation()})"