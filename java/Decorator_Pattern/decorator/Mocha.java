package java.Decorator_Pattern.decorator;

import beverage.Beverage;

public class Mocha extends CondimentDecorator {
    
    public Mocha(Beverage beverage){
        this.beverage = beverage;
    }

    @Override
    public double cost(){
        return beverage.cost() + .20;
    }

    @Override
    public String getDescription(){
        return beverage.getDescription() + ", Mocha";
    }
}
