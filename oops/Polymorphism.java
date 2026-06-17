class Vehicle {
    String brand;

    Vehicle(String brand) {
        this.brand = brand;
    }

    void start() {
        System.out.println(brand + " starts");
    }
}

class Car extends Vehicle {
    Car(String brand) {
        super(brand);
    }

    @Override
    void start() {
        System.out.println(brand + " the car starts");
    }
}

class Bike extends Vehicle {
    Bike(String brand) {
        super(brand);
    }

    @Override
    void start() {
        System.out.println(brand + " the bike starts");
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        Vehicle v = new Vehicle("MG");
        v.start();
        Car c = new Car("Venue");
        c.start();
        Bike b = new Bike("Kwid");
        b.start();
    }
}