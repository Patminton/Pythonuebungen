print('Einfacher Taschenrechner')
v1= input('Erste Zahl? ')
op= input('Operation? ')
v2= input('Zweite Zahl? ')

if v1.isnumeric() == False or v2.isnumeric() == False:
    print('Bitte geben Sie eine Zahl ein.')
    exit()

v1 = int(v1)
v2 = int(v2)
if op == '+':
    print('Summe von {} {} {} ist {}'.format(v1,op,v2,v1+v2))
elif op == '-':
    print('Differenz von {} {} {} ist {}'.format(v1,op,v2,v1-v2))
elif op == '*':
    print('Produkt von {} {} {} ist {}'.format(v1,op,v2,v1*v2))
elif op == '/':
    print('Quotient von {} {} {} ist {}'.format(v1,op,v2,v1/v2))
elif op == '^':
    print('Exponent von {} {} {} ist {}'.format(v1,op,v2,v1^v2))
elif op == '%':
    print('Rest von {} {} {} ist {}'.format(v1,op,v2,v1%v2))
else:
    print('Operator nicht erkannt')
print('fertig')
