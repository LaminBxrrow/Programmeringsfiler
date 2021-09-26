#Skapat den: 05/09-21
#Av: Lamin barrow
namn=input("Hej, vad heter du?: ")
svar=input(("Hej "+namn+", hur kul ska det bli att lära sig att programmera(1-10)?: "))
kulfaktor = 7

while int(svar)<kulfaktor:
    print("Blir det det inte roligare än en " + str(svar) + ":a?: ")
    svar=int(input('Hur roligt ska det bli att programmera (1-10)? '))
print ("Så kul!")



