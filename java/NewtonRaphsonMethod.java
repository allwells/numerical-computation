package java;
public class NewtonRaphsonMethod {

    private static void println(Object object) {
        System.out.println(object);
    }

    private static double round(double value) {
        double result = (double) Math.round(value * 1000000) / 1000000D;
        return result;
    }

    public static void main(String[] args) {
        // Formula: Xn+1 = Xn + C/Xn

        double X0 = 2;
        double C = 5;

        println("Formula: Xn+1 = Xn + C/Xn\n");
        println("X0: " + X0);
        for (int n = 1; n < 11; n++) {
            double Xn = (X0 + (C /X0))/2;
            if (Xn == X0) {
                break;
            } else {
                println("X"+ n + ": " + round(Xn));
                X0 = Xn;
            }
        }
    }
}
