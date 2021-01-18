import random

ran = random.randint(1,5)
count = 0
val = 0
while val != ran :
    val=input('Geben Sie eine Zahl zwischen 1 und 5 ein: ')
    count += 1
    if val.isnumeric():
        val=int(val)
    else:
        continue

else :
    print(f'Du hast es in {count} Versuchen erraten')
    
    
