from math import cos
from texttable import Texttable

X0 = float(input('Enter value for Xo: '))
X1 = float(input('Enter value for X1: '))
iteration = int(input('Enter number of iteration to make: '))

def f(x):
    result = x - cos(x)
    return result



table = Texttable()
table.header(['i','Xo', 'X1', 'f(Xo)', 'f(X1)'])

print('\nf(Xo):', f(X0))
print('f(X1):', f(X1), '\n')
table.add_row([1, X0, X1, f(X0), f(X1)])

for count in range(2, iteration):
    nominator = (X0 * f(X1)) - (X1 * f(X0))
    denominator = f(X1) - f(X0)

    try:
        Xn = nominator / denominator
        # print('X' + str(count) + ':', Xn)
        X0 = X1
        X1 = Xn
        table.add_row([count, X0, X1, f(X0), f(X1)])
    except ZeroDivisionError:
        print('Math Error!\nCannot divide by Zero!')
        break

print(table.draw())