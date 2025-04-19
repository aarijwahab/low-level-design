package java.Adapter_Pattern.turkey;

public class WildTurkey implements Turkey {
    public void fly(){
        System.out.println("Flap");
    }

    public void gobble(){
        System.out.println("Gobble Gobble");
    }
}
