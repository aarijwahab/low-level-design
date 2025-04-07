package ducks;

import fly.FlyNoWay;
import quack.Quack;

public class ModelDuck extends Duck {

    public ModelDuck(){
        flyBehaviour = new FlyNoWay();
        quackBehaviour = new Quack();
    }

    @Override
    public void display() {
        System.out.println("I am but a model duck.");
    }
    
}
