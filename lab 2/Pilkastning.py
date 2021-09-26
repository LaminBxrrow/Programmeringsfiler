# Pilpoäng av Lamin Barrow
# Skrivet den 12/9-2021

namn1=input("Vad heter kastare 1?: ")          #introducerar variabel för spelare nummer 1
namn2=input("Vad heter kastare 2?: ")          #introducerar variabel för spelare nummer 2

poang1=[]                                                    #Listor för spelarnas resultat:
poang2=[]
                                         #Variabel för summor behövs så att elementen i listorna kan adderas till ett resultat
summa_namn1=0
summa_namn2=0

for i in range(5):
    poang=int(input("Vilken poäng fick "+namn1+" på kast nr "+str(i+1)))
    poang1.append(poang)
    summa_namn1+=int(poang1[i])
#Denna for slinga sätter användarens svar 1 i taget in i listan poang1, elementen i poang1 adderas till en summa.

for i in range(5):
    poang2.append(int(input("Vilken poäng fick "+namn2+" på kast nr "+str(i+1))))
    summa_namn2+=int(poang2[i])
# Fungerar exakt likadant som första for-slingan. Däremot kommer den att fungera för spelare 2 istället.

if summa_namn1==summa_namn2:
    print("Ingen vinnare kan utses då "+ namn1+' och '+ namn2+' fick totalt sett samma poäng (det blir oavgjort)')
if summa_namn1<summa_namn2:
   print(" Vinnaren av pilkastningen är "+ namn2+ ', Bra spelat!')

if summa_namn1>summa_namn2:
    print(" Vinnaren av pilkastningen är "+ namn1+ ', Bra spelat!')
#  I if slingorna görs en bedömning av hur summorna förhåller sig till varandra, det finns tre scenarion-> 3 if slingor.
#går säkert att skriva på ett lättare sätt dock.

