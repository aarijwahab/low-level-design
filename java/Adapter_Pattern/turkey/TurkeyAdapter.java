package java.Adapter_Pattern.turkey;

import Adapter_Pattern.duck.Duck;

public class TurkeyAdapter implements Duck {
    Turkey turkey;

    public TurkeyAdapter(Turkey turkey){
        this.turkey = turkey;
    }

    public void fly(){
        for (int i = 0; i < 5; i++){
            turkey.fly();
        }
    }

    public void quack(){
        turkey.gobble();
    }
    
}
