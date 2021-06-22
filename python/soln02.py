# Formula: Xn+1 = Xn + C/Xn


X0 = float(input('Enter value for X0: '))
C = float(input('Enter value for C: '))

print('Formula: Xn+1 = Xn + C/Xn\n')
print('X0:', X0)

for n in range(1,12):
    Xn = (X0 + (C / X0)) / 2
    if Xn == X0:
        break
    else:
        print('X' + str(n) +':',round(Xn, 6))
        X0 = Xn

