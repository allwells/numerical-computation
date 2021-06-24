#include <iostream>
using namespace std;

int main() {
    // Formula: Xn+1 = Xn + C/Xn
    float X0 = 2;
    float C = 5;
    cout << "Formula: Xn+1 = Xn + C/Xn\n";
    cout << "X0: " << X0;

    for (int n = 1; n < 12; n++) {
        float Xn = (X0 + (C / X0)) / 2;
        if (Xn == X0) {
            break;
        } else {
            cout << "\nX" << n << ": " << Xn;
            X0 = Xn;
        }

    }
    cout << "\n";
    return 0;
}