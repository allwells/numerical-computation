from prettytable import PrettyTable
# Formula: Xn+1 = Xn + C/Xn

table = PrettyTable()
table.field_names = ['x', 'Solution']

Xo = float(input('Enter value for X0: '))
C = float(input('Enter value for C: '))

print('Xo:', Xo)
print('C :', C)

for n in range(1,12):
    Xn = (Xo + (C / Xo)) / 2
    if Xn == Xo:
        table.add_row([n, '[ ' + str(Xn) + ' ]'])
        break
    else:
        table.add_row([n, Xn])
        Xo = Xn

print(table)