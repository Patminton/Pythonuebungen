value=input('Was ist die Temperatur in Fahrenheit?: ')

if value.isnumeric() == False:
    print('Eingabe ist keine Nummer')
    exit()

celsius = ((int(value))-32)* 5/9
print('Temperatur in Celsius is: ',int(celsius))