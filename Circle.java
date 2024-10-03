import java.util.Scanner;

public class Circle {
    private double radius;

    // Constructor to initialize the radius
    public Circle(double radius) {
        this.radius = radius;
    }

    // Method to calculate the area of the circle
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the radius of the circle: ");
        double radius = scanner.nextDouble();

        // Create an instance of the Circle class
        Circle circle = new Circle(radius);

        // Check if the radius is greater than 20
        if (radius > 20) {
            // Calculate and display the area of the circle
            double area = circle.calculateArea();
            System.out.println("Area of the circle: " + area);
        } else {
            System.out.println("Radius should be greater than 20.");
        }

        scanner.close();
    }
}
