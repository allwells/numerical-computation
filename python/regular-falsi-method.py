from math import fabs

a = float(input('Enter lower guess, a: '))
b = float(input('Enter upper guess, b: '))
e = float(input('Enter tolerable error, e: '))

def f(x):
    result = (x * x * x) + (3 * x) - 5

    return result




while fabs(f(c)) > e:
    c = b - (f(b) * (b - a)) / (f(b) - f(a))

    if (f(a) * f(b)) < 0:
        b = c
    else:
        a = c

