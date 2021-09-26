''' Skriven av : Lamin Barrow & Melker Haglund
19/09.-21'''

#Hälsar användaren välkomna till programmet
def introduktion_till_program():
    hälsning = "Välkommen till vårt glosprogram. Här ska du översätta några ord som är givna på svenska till vad de betyder på franska. "
    return hälsning

"""Denna funktion gör själva förhöret av glosan. I paramatrarna finns både det svenska och franska ordet. 
   Funktionen fungera som så att inputen jämförs med den franska glosan. Om if-satsen blir 'true' så 
   kommer koden under den att köras, annars körs koden under else att köras. Sedan så kommer både if och else
   med en liten kommentar som visar om användaren översatt ordet korrekt."""
def glosförhör(Svensk_glosa, Franska_glosa):
    gissning = input('Vad är den Franska översättningen för '+Svensk_glosa+"?: ")

    if gissning.lower() == Franska_glosa:
        respons_gissning = 'Très Bien!'
        print(respons_gissning)
    else:
        respons_gissning = "Malheureusement! Rätt svar är: " + Franska_glosa
        print(respons_gissning)
    return respons_gissning

'''Denna funktion använder sig av funktionen glosförhör för att räkna antalet rätt användaren fick
 genom att jämföra return-värdet från glosförhör med den respons som fås om man svarat korrekt.
  Om dessa är lika adderas en poäng till summan. Detta görs för varje element inom listorna.
   Den returnar sedan summan dvs antalet rätt som skrivs ut m.h.a en print-sats som finns
   inom main funktionen.'''
def summering_av_svar(språk1,språk2):
    antal_rätt = 0
    for i in range(len(språk1)):
        if glosförhör(språk1[i], språk2[i])=='Très Bien!':
            antal_rätt+=1
    return antal_rätt

#Ser till att det inte finns några globala variabler i namnet.
def main():
    Franska_lista = ["maintenant", "ordinateur", "vélo", "boulangerie", "voleur", "suède"]
    Svenska_lista = ["nu", "dator", "cykel", "bageri", "tjuv", "Sverige"]
    print("Du har fått", summering_av_svar(Svenska_lista, Franska_lista), "rätt av", len(Svenska_lista))

main()




