from texttable import Texttable
from numpy import sign

a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
h = float(input('Enter value for tolerance, h: '))
n_max = int(input('Enter max number of iterations: '))

def f(x):
    result = 10 - (x**2)
    return result


print('\na:   ', a)
print('b:   ', b)
print('f(a):', f(a))
print('f(b):', f(b),'\n')

table = Texttable()
table.header(['i', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])

for i in range(0, n_max):
    c = (a + b) / 2

    if f(c) != 0:
        if (abs(f(c) > h)) and (i <= n_max):
            if sign(f(c)) == sign(f(a)):
               a = c
               b = b
            else:
                a = a
                b = c
            
            c = (a + b) / 2
            # i += 1
            
        else:
            print(c, 'is the root of the function')
            break
        
        # if f(c) < 0:
        #     a = c
        #     b = b
        # else:
        #     a = a
        #     b = c
    else:
        print(c, 'is the root of the function')
        break
    
    table.add_row([i, a, b, c, f(a), f(b), f(c)])


print(table.draw())
