abstract class Shape {
    abstract void area();
}

class Circle extends Shape {
    int r;

    Circle(int r) {
        this.r = r;
    }

    void area() {
        System.out.println(3.14 * r * r);
    }
}

class Rectangle extends Shape {
    int l;
    int b;

    Rectangle(int l, int b) {
        this.l = l;
        this.b = b;
    }

    void area() {
        System.out.println(l * b);
    }
}

public class Abstraction {
    public static void main(String[] args) {
        Circle c = new Circle(2);
        Rectangle r = new Rectangle(2, 3);
        c.area();
        r.area();
    }
}