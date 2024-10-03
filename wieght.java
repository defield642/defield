public class WeightComparison {
    double weight1;
    double weight2;
    double weight3;

    public WeightComparison(double weight1, double weight2, double weight3) {
        this.weight1 = weight1;
        this.weight2 = weight2;
        this.weight3 = weight3;
    }

    public double findSmallestWeight() {
        double smallest = weight1;

        if (weight2 < smallest) {
            smallest = weight2;
        }

        if (weight3 < smallest) {
            smallest = weight3;
        }

        return smallest;
    }

    public static void main(String[] args) {
        WeightComparison weights = new WeightComparison(50.5, 45.3, 55.7);
        double smallestWeight = weights.findSmallestWeight();
        System.out.println("The smallest weight is: " + smallestWeight);
    }
}
