from component import Component

class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    
    def operation(self):
        return "Concrete Operation"
