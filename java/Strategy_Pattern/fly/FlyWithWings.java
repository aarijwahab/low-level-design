package java.Strategy_Pattern.fly;

public class FlyWithWings implements FlyBehaviour{
    @Override
    public void fly() {
        System.out.println("I am flying with wings!");   
    }
}
