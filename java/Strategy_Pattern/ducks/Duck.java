package java.Strategy_Pattern.ducks;

import fly.FlyBehaviour;
import quack.QuackBehaviour;

public abstract class Duck{
    QuackBehaviour quackBehaviour;
    FlyBehaviour flyBehaviour;

    public void performQuack(){
        quackBehaviour.quack();
    }

    public void performFly(){
        flyBehaviour.fly();
    }

    public void swim(){
        System.out.println("All ducks can float, even decoys    !");
    }

    public void setFlyBehaviour(FlyBehaviour fb){
        flyBehaviour = fb;
    }

    public void setQuackBehaviour(QuackBehaviour qb){
        quackBehaviour = qb;
    }

    public abstract void display();
}