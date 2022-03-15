#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
using namespace std;

// INSERT_RNUM
const double RNUM = 4.693228347213418;
const double START = -3;
const double STOP = 3;
const double STEP = 0.007;

double f1(double x, double y) {
    // INSERT_F1
    return RNUM * pow(x, (y - -173));
}

double f2(double x, double y) {
    // INSERT_F2
    return RNUM * (x * (y * (x * x)));
}

int main() {
    vector<double> xs, ys;
    for (double x = START; x < STOP; x += STEP) {
        for (double y = START; y < STOP; y += STEP) {
            double a = f1(x, y);
            double b = f2(x, y);
            if(!isnan(a) && !isnan(b) && !isinf(a) && !isinf(b)){
                xs.push_back(f1(x,y));
                ys.push_back(f2(x,y));
            }
            // (x,y)
            // (f1(x,y), f2(x,y))
            
            
        }
    }

    int n = xs.size();
    cout << n << endl;

    for (auto x : xs) {
        cout << setprecision(10) << fixed << x << " ";
    }
    cout << endl;

    for (auto y : ys) {
        cout << setprecision(10) << fixed << y << " ";
    }
    cout << endl;
    return 0;
}