package Observer_Pattern;

import Observer_Pattern.observer.CurrentConditionsDisplay;
import Observer_Pattern.subject.WeatherData;

public class WeatherStation {

    public static void main(String [] args){
        WeatherData weatherData = new WeatherData();
        CurrentConditionsDisplay currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);

        weatherData.setMeasurements(20, 35, 30.2f);
        weatherData.setMeasurements(30, 25, 30.2f);
        weatherData.setMeasurements(40, 15, 30.2f);
    }
}
