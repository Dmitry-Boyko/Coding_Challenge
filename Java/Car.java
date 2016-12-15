import java.lang.*;
import java.util.*;

public class Car {
    public enum CarType { Sport, Sedan, Hybrid, Luxury, Racing };
    public enum Color { Red, Black, White, Gray };

    private final CarType carType;
    private final Color color;
    private final int doors;
    private final String engineType;
    private int wheelDiameter;
    private Hashtable<String, Integer> tireSize;

    /**
     * Constructor.
     */
    public Car(CarType carType, Color color, int doors, String engine) {
        this.carType = carType;
        this.color = color;
        this.doors = doors;
        this.engine = engine;
    }


    // Getters
    public CarType getCarType() {
        return this.carType;
    }

    public Color getColor() {
        return this.color;
    }

    public int getDoors() {
        return this.doors;
    }

    public String getEngineType() {
        return this.engineType;
    }

    public int getWheelDiameter() {
        return this.wheelDiameter;
    }

    public Hashtable<String, Integer> getTireSize() {
        return this.tireSize;
    }

    
    // Setters
    public void setWheelDiameter(int wheelDiameter) {
        if ((wheelDiameter < 15) || (wheelDiameter > 19)) {
            throw new IllegalArgumentException();
        }

        this.wheelDiameter = wheelDiameter;
    }

    public void setTireSize(Hashtable<String, Integer> tireSize) {
        if ((tireSize == null) || !tireSize.containsKey("Width") || !tireSize.containsKey("Height")) {
            throw new IllegalArgumentException();
        }

        this.tireSize = tireSize;
    }
}