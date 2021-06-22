package java;
public class soln02 {

    private static void println(Object object) {
        System.out.println(object);
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
                println("X"+ n + ": " + (double) Math.round(Xn * 1000000) / 1000000D);
                X0 = Xn;
            }
        }
    }
}
