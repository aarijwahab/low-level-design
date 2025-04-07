import pizza.Pizza;
import store.ChicagoPizzaStore;
import store.NyPizzaStore;

public class PizzaTestDrive {
    public static void main(String[] args){
        NyPizzaStore nyPizzaStore = new NyPizzaStore();
        ChicagoPizzaStore chicagoPizzaStore = new ChicagoPizzaStore();

        Pizza pizza = nyPizzaStore.orderPizza("cheese");
        System.out.println("Ethan ordered a " + pizza.getName() + "\n");
        
        pizza = chicagoPizzaStore.orderPizza("cheese");
        System.out.println("Joel ordered a " + pizza.getName() + "\n");
    }   
}
