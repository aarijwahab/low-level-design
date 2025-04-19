from .fly_behaviour import FlyBehaviour

class RocketFlyBehaviour(FlyBehaviour):

    def fly(self) -> None:
        print("I'm flying with rocket boosters!")