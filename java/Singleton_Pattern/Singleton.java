package java.Singleton_Pattern;
public class Singleton {
    private static Singleton uniqueInstance;

    private Singleton(){}


    // For race conditions this will need to be synchronized
    public static Singleton getInstance(){
        if (uniqueInstance == null){
            uniqueInstance = new Singleton();
        }

        return uniqueInstance;
    }
}
