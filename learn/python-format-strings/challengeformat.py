first_value = '  FIRST challenge         ' #27 sollen es sein und sind bisher 26, 7 links frei 8 rechts
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
help= first_value.strip()
help1=help.lower()
help2=help1.title()
help3= help2.rjust(22)
ausgabe= f'{help3:<29}'
print(ausgabe)

# Second challenge
h=second_value.replace('-',' ')
h=h.strip()
h=h.capitalize()
print(h)

# Third challenge
h=third_value.replace(' ','')
h=h.lower()
h=h.capitalize()
h=h.replace('-',' ')
print(h.rjust(30))

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value+'#'+fifth_value+'#'+sixth_value+'!')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')