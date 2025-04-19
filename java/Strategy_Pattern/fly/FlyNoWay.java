package java.Strategy_Pattern.fly;

public class FlyNoWay implements FlyBehaviour{

    @Override
    public void fly() {
        System.out.println("I cant fly!");
    }
    
}
