package store;
import pizza.NyStyleCheesePizza;
import pizza.Pizza;

public class NyPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        if (type.equals("cheese")){
            return new NyStyleCheesePizza();
        } else {
            return null;
        }

    }
    
}
