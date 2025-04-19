package java.Strategy_Pattern;
import ducks.Duck;
import ducks.MallardDuck;
import ducks.ModelDuck;
import fly.FlyRocketPowered;

public class DuckSimulator {
    public static void main(String [] args){
        Duck mallard = new MallardDuck();
        mallard.performQuack(); 
        mallard.performFly();

        Duck model = new ModelDuck();
        model.performFly();
        model.setFlyBehaviour(new FlyRocketPowered());
        model.performFly();
    }    
}
