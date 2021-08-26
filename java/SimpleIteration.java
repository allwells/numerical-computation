package java;

class SimpleIteration {

    private static void println(Object object) {
        System.out.println(object);
    }
    
    private static void print(Object object) {
        System.out.print(object);
    }

    private static double round(double value) {
        double result = Math.round((value * 1000000000) / 1000000000D);
        return result;
    }

    public static void main(String[] args) {
        java.util.Scanner scan = new java.util.Scanner(System.in);

        print("Enter value for Xo: ");
        double Xo = scan.nextDouble();

        for(int n=1; n < 12; n++) {
            Xo = round(Math.cos(Xo));
            println("X" + n + " = cosX" + (n-1) + " = " + Xo);
        }
    }
}