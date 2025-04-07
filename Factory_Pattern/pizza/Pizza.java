package pizza;

import java.util.ArrayList;
import java.util.List;

public abstract class Pizza {
    String name;
    String dough;
    String sauce;
    List<String> toppings = new ArrayList<String>();
    
    public void prepare(){
        System.out.println("Preparing " + name);
        System.out.println("Tossing dough..."); 
        System.out.println("Adding sauce..."); 
        System.out.println("Adding toppings: "); 
        for (String topping : toppings) { 
            System.out.println("" + topping); 
        }
    }

    public void bake() {
        System.out.println("Bake for 25 min at 350");
    }

    public void cut(){
        System.out.println("Cutting pizza by diagonals");
    }

    public void box(){
        System.out.println("Place pizza in official pizza box");
    }

    public String getName(){
        return name;
    }
}
