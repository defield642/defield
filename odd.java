public class SumOfOddNumbers {
    public static void main(String[] args) {
        // Initialize variables
        int sum = 0;

        // Iterate through numbers from 15 to 70
        for (int i = 15; i <= 70; i++) {
            // Check if the number is odd
            if (i % 2 != 0) {
                // Add the odd number to the sum
                sum += i;
            }
        }

        // Print the sum of odd numbers
        System.out.println("Sum of odd numbers between 15 and 70: " + sum);
    }
}
