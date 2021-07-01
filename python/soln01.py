import math

h = 0.2
a = 1
b = math.pi / 2

def f(value):
    result = value  - math.cos(value)
    return round(result, 4)

def ce(a, b):
    result = (a + b) / 2
    return round(result, 4)


while (b - a) > h:
    c = ce(a, b)
    print('C =', round(c, 4))

    if (f(b) * f(a)) > 0:
        a = c
        print('New A:', round(a, 4))
    else:
        b = c
        print('New B:', round(b, 4))
    
    print('b - a =', round((a - b), 4), "\n\n")
