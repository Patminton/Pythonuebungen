print("Mochten Sie fortfahren?")
answer= input()
if answer == "n" or answer =="no":
    print("Aufregend")
elif answer == "y" or answer =="yes":
    print("Weiter geht's..."+'\n'+b"Fertig!")
    #print("Fertig!")
else:
    print("Bitte versuchen Sie es nochmal mit yes oder no")
