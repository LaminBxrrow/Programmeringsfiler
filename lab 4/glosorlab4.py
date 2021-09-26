''' Skriven av : Lamin Barrow & Melker Haglund
26/09.-21'''

# Hälsar användaren välkomna till programmet


def introduktion_till_program():

    hälsning = "Välkommen till vårt glosprogram. Här ska du översätta några ord som är givna på svenska till vad de betyder på franska. "
    return hälsning


'''Öppnar filen textfilen glosord och läser den.Encoding="utf-8" gör att tecken såsom è läses av korrekt i programmet. Sedan tas radbytes tecknet ('\n'). Då fås en lista (lista_på_filinnehåll med två element där varje element
motsvarar en rad i filen glosord. Filen glosord är strukturerad så att de svenska orden är på rad 1 (dvs index nr 0 i listan) och franska orden i rad 2 (index nr 1).
 I textfilen finns det mellanrum mellan orden och därför kommer listapåfilinnehåll[(index)].split('') att separera varje ord till ett eget element och dessa sparar vi till Svenska lista
 respektive Franska listan.'''


def Glosor():

    with open('glosord.txt', 'r', encoding="utf-8") as file:
        helafilen = file.read()
        lista_på_filinnehåll = helafilen.split('\n')
        Svenskalistan = lista_på_filinnehåll[0].split(' ')
        Franskalistan = lista_på_filinnehåll[1].split(' ')

    return Franskalistan, Svenskalistan


"""Denna funktion gör själva förhöret av glosan. I paramatrarna finns både det svenska och franska ordet.
   Funktionen fungera som så att inputen jämförs med den franska glosan. Om if-satsen blir 'true' så
   kommer koden under den att köras, annars körs koden under else att köras. Sedan så kommer både if och else
   med en liten kommentar som visar om användaren översatt ordet korrekt."""


def glosförhör(Svensk_glosa, Franska_glosa):
    gissning = input('Vad är den franska översättningen för '+Svensk_glosa+"?: ")

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


def summering_av_svar(språk1, språk2):

    antal_rätt = 0
    for i in range(len(språk1)):
        if glosförhör(språk1[i], språk2[i]) == 'Très Bien!':
            antal_rätt += 1

    return antal_rätt

# Ser till att det inte finns några globala variabler i namnet.


def main():

    print(introduktion_till_program())
    franska_glosorden, svenska_glosorden = Glosor()
    print("Du har fått", summering_av_svar(svenska_glosorden,
          franska_glosorden), "rätt av", len(franska_glosorden))


main()
