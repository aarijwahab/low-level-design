from ducks.duck import Duck
from ducks.mallard_duck import MallardDuck
from ducks.model_duck import ModelDuck
from fly.fly_behaviour import FlyBehaviour
from fly.rocket_fly_behaviour import RocketFlyBehaviour
from fly.wings_fly_behaviour import WingsFlyBehaviour

class DuckDemo():
    def run(self):
        mallardDuck: Duck = MallardDuck()
        modelDuck: Duck = ModelDuck()

        print("Mallard duck")
        mallardDuck.setFlyBehaviour(WingsFlyBehaviour())
        mallardDuck.display()
        mallardDuck.performFly()

        print("Current model duck behaviour")
        modelDuck.setFlyBehaviour(RocketFlyBehaviour())
        modelDuck.display()
        modelDuck.performFly()

        print("New model duck behaviour")
        modelDuck.setFlyBehaviour(WingsFlyBehaviour())
        modelDuck.display()
        modelDuck.performFly()

        print("We were able to change the model duck's fly behaviour at runtime!")

if __name__ == "__main__":
    duckDemo = DuckDemo()
    duckDemo.run()