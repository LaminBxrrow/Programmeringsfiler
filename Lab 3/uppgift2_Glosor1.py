# Skapades av: Lamin Barrow & Melker Haglund
# Skapades den: 17/9 2021
def introduktion():
    print(
        "Välkommen till mitt glosprogram. Här ska du översätta några ord som är givna på svenska till vad de betyder på franska. ")


# Funktionen 'introduktion' är en enkel funktion som introducerar glosprogrammet till användaren m.h.a en print-sats.
introduktion()

# listor av orden på både språken
Franska_lista = ["maintenant", "ordinateur", "vélo", "boulangerie", "voleur", "suède"]
Svenska_lista = ["nu", "dator", "cykel", "bageri", "tjuv", "Sverige"]
# Variablerna som är givna här används för att visa användaren hur många rätt dem fått på glosförhöret.
rätt_total = str(len(Svenska_lista))
antal_rätt = len(Svenska_lista)
# for-slingan itererar igenom alla element i listan och låter användaren skriva en översättning till varje element.
# Efter att ha pratat med min sammarbetspartner Lamin Barrow så inser jag att jag skulle kunnat använda "len(Svenska_lista)"" istället för "Svenska_lista.index(Svenska_lista[-1])+1"
for i in range(len(Svenska_lista)):
    Gissning = input("Skriv den franska översättningen till ordet '" + Svenska_lista[i] + "': ")
    Översättning = Gissning.lower()
    if Översättning == Franska_lista[i]:
        print("Très Bien!")
    else:
        print("Malheureusement! Rätt svar är: " + Franska_lista[i])
        antal_rätt = antal_rätt - 1
# Sedan så visar "antal_rätt" att för varje fel svar användaren har så drar programmet av en poäng från antalet rätt.

print(str(antal_rätt) + " av " + rätt_total)
