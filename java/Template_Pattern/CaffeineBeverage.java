package java.Template_Pattern;

public abstract class CaffeineBeverage {
    
    final void prepareRecipe(){
        boilWater();
        brew();
        pourInCup();
        if (customerWantsCondiments()){
            addCondiments();
        }
    }

    abstract void brew();

    abstract void addCondiments();

    void boilWater(){
        System.out.println("Boiling the water");
    }

    void pourInCup(){
        System.out.println("Pouring into the cup");
    }

    boolean customerWantsCondiments(){
        return true;
    }
}
