package java.Strategy_Pattern.ducks;

import fly.FlyWithWings;
import quack.Quack;

public class MallardDuck extends Duck{
    public MallardDuck(){
        quackBehaviour = new Quack();
        flyBehaviour = new FlyWithWings();
    }

    public void display(){
        System.out.println("I'm a real Mallard duck.");
    }
}
