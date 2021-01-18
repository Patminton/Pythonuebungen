import random
farben = ['Herz', 'Gras', 'Karo', 'Kreuz']
karten = ['2','3','4','5','6','7','8','9','10','Bube','Dame','König','Ass']
cards=[]
for farbe in farben:
    for karte in karten:
        karte = farbe+' '+karte
        cards.append(karte)
print(f'Es gibt {len(cards)} Karten in dem Deck') 
print(f'Dealing...')
hand =[]

while len(hand)<5 :
   
    newcard=random.choice(cards)
    cards.remove(newcard)
    hand.append(newcard)
else:
    print(f'Es gibt {len(cards)} Karten im Deck')
    print(f'der Spieler hat die folgenden Karten auf der Hand:\n {hand}')