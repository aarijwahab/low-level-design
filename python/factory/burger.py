from abc import ABC, abstractmethod

class Burger(ABC):
    
    @abstractmethod
    def prepare(self):
        pass
