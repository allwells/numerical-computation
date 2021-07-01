import math
X0 = float(input('Enter value for Xo: '))
for n in range(1, 12):
    X0 = round(math.cos(X0), 10)
    print('X' + str(n) + ' = cosX' + str(n-1) + ' = '+ str(X0))
