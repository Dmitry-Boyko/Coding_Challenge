// --- Task ------------------------------------------------------------------------------------------------
// Design a car class that describes properties of cars
// code should compile and run

// FIELDS
// -> car type
// -> color
// -> doors
// -> engine type (ex: "2.0L", "2.0L HO", "2.6L", "3.0L", "3.0L Turbo")
// -> wheel diameter (ex: 15, 16, 17, 18)
// -> tire size (ex: 185x50, 195x45, 205x40)
//
// REQUIREMENTS:
// -> mandatory constructor arguments: 
//    * car type (should be an Enum, options: Sport, Sedan, Hybrid, Luxury, Racing)
//    * color    (should be an Enum, options: Red, Black, White, Gray)
//    * doors    (should be an integer)
//    * engine   (should be a string)
//
// -> all fields should be accessed via getters
// -> provide setters for wheelDiameter and tireSize
// -> wheel diameter should be an integer. do not allow wheel sizes less than 15 or greater than 19.
// -> tire size should be a Dictionary, e.g. {"Width": 185, "Height": 50}

// --- My Result -------------------------------------------------------------------------------------------


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