package java;
public class soln01 {

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

    public static void main(String[] args) {
        java.util.Scanner scan = new java.util.Scanner(System.in);
        final double h = 0.2;
        print("Enter value for a: ");
        double a = scan.nextDouble();
        double b = Math.PI / 2;

        while(((b - a) > h)) {
            double c = c(a, b);
            println("C = " + Math.round(c * 100) / 100D);
            println("b - a = " + (double) Math.round((a - b) * 100) / 100D);

            if ((f(b) * f(a) > 0)) {
                a = c;
                println("New A: " + (double) Math.round(a * 100) / 100D);
            } else {
                b = c;
                println("New B: " + (double) Math.round(b * 100) / 100D);
            }

            println("b - a = " + (double) Math.round((a - b) * 100) / 100D + "\n\n");
        }
        
        println("End iteration...");
        scan.close();

    }
}