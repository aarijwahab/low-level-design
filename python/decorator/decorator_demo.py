
from component import Component
from decorator import Decorator
from concrete_component import ConcreteComponent
from concrete_decorator_a import ConcreteDecoratorA
from concrete_decorator_b import ConcreteDecoratorB

class DecoratorDemo:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    def run(self, component: Component):
        print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    client = DecoratorDemo()
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client.run(simple)
    print("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    client.run(decorator2)