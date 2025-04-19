package java.Factory_Pattern.store;
import pizza.ChicagoStyleCheesePizza;
import pizza.Pizza;

public class ChicagoPizzaStore extends PizzaStore {

    Pizza createPizza(String type) {
        if (type.equals("cheese")){
            return new ChicagoStyleCheesePizza();
        } else{
            return null;
        }
    }
    
}
