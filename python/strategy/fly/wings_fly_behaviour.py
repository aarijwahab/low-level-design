from .fly_behaviour import FlyBehaviour

class WingsFlyBehaviour(FlyBehaviour):

    def fly(self) -> None:
        print("I'm flying with my real wings!")