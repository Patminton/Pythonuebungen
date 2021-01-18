import random

value = random.randint(1,10)
guess = 0
count = 0
while guess!= value:
    guess = input('Raten Sie eine Nummer zwischen 1 und 10: ')
    count += 1
    print(f'Eingabe im Versuch #{count}: {guess}')
    if not(guess.isnumeric()):
        print('Nur Zahlen bitte!')
        continue
    else:
        guess=int(guess)

    if guess<value:
        print('Sie haben zu niedrig geraten, neuer Versuch!')
        continue
    elif guess>value:
        print('Sie haben zu hoch geraten, neuer Versuch!')
else:
    print(f'Sie haben es in {count} Versuchen erraten, die gesuchte Zahl war {value}######')
    
