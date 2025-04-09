package Adapter_Pattern.duck;

public class MallardDuck implements Duck {
    public void quack(){
        System.out.println("Quack Quack!");
    }

    public void fly(){
        System.out.println("I'm flying high!");
    }
}
