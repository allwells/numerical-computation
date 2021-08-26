package java;
public class BisecetionMethod {

    private static void println(Object object) {
        System.out.println(object);
    }

    private static void print(Object object) {
        System.out.print(object);
    }

    private static double f(double value) {
        double result = value - Math.cos(value);
        return result;
    }

    private static double c(double a, double b) {
        double result = (a + b)/2;
        return result;
    }

    private static double round(double value) {
        double result = (double) Math.round((value * 10000) / 10000D);
        return result;
    }

    public static void main(String[] args) {
        java.util.Scanner scan = new java.util.Scanner(System.in);
        final double h = 0.2;
        print("Enter value for a: ");
        double a = scan.nextDouble();
        double b = Math.PI / 2;

        while(((b - a) > h)) {
            double c = c(a, b);
            println("C = " + round(c));
            println("b - a = " + round(a - b));

            if ((f(b) * f(a) > 0)) {
                a = c;
                println("New A: " + round(a));
            } else {
                b = c;
                println("New B: " + round(b));
            }

            println("b - a = " + round((a - b)) + "\n\n");
        }
        
        println("End iteration...");
        scan.close();

    }
}