package java.Observer_Pattern.subject;

import Observer_Pattern.observer.Observer;

public interface Subject {
    public void registerObserver(Observer o);
    public void removeObserver(Observer o);
    public void notifyObservers();    
}
