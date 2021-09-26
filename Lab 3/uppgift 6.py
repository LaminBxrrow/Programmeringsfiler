def introduktion():
    print("Välkommen till mitt glosprogram. Här ska du översätta några ord"
          " som är givna på svenska till vad de betyder på franska. ")
#
introduktion()

def f1(Svenska_lista,Franska_lista):
    for i in range(len(Svenska_lista)):
        Gissning = input("Skriv den franska översättningen till ordet '" + Svenska_lista[i] + "': ")
        if Gissning.lower()== Franska_lista[i]:
            print("Très Bien!")
        else:
            print("Malheureusement! Rätt svar är: " + Franska_lista[i])

#f1(['hej','morgon'],['salut','matin'])
