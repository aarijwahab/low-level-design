from abc import ABC, abstractmethod
from fly.fly_behaviour import FlyBehaviour

class Duck(ABC):

    def __init__(self):
        self.flyBehaviour: FlyBehaviour = None
    
    def setFlyBehaviour(self, flyBehaviour: FlyBehaviour):
        self.flyBehaviour = flyBehaviour
    
    def performFly(self):
        self.flyBehaviour.fly()

    def swim(self) -> None:
        print("I'm swimming")

    @abstractmethod
    def display(self) -> None:
        pass