class Animal {
    String name;

    Animal(String name) {
        this.name = name;
    }

    void sound() {
        System.out.println(name + " makes a sound");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + " barks");
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Animal a = new Animal("Cat");
        a.sound();
        Dog d = new Dog("Bruno");
        d.sound();
    }
}