#include <stdio.h>

int main() {
    // Formula: Xn+1 = Xn + C/Xn
    float X0 = 2;
    float C = 5;
    printf("Formula: Xn+1 = Xn + C/Xn\n");
    printf("X0: %f\n", X0);

    for (int n = 1; n < 12; n++) {
        float Xn = (X0 + (C / X0)) / 2;
        if (Xn == X0) {
            break;
        } else {
            printf("X%d", n, ": %9.6f\n", Xn);
            X0 = Xn;
        }
    }

    return 0;
}