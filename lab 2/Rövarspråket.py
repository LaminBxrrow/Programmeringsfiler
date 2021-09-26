# Rovarspråk av Lamin Barrow
# Skrivet den 12/9-2021
konsonanter=["b","c","d","f","g","h","j","k","l","m",'n','p','q','r','s','t','v','w','x','z']
#ändrar till en lista för att det i teorin inte spelar någon roll, (är bekvämare med lista dock)
print("Hej och välkommen till rövarspråksöversättaren")

svenska=input("Skriv in det du vill översätta till rövarspråket: ")
case_sensitivity=svenska.lower()
#För att översättningen ska bli korrekt måste det användaren skriver in vara i små bokstäver, därav omvandlingen.
rövarspråk=''

for i in range(len(case_sensitivity)):
        if case_sensitivity[i] in konsonanter:
            bokstav=case_sensitivity[i]+'o'+case_sensitivity[i]
            rövarspråk+=bokstav
        else:
            vokal=case_sensitivity[i]
            rövarspråk+=vokal
#for slingan  fungerar så att den kontrollerar en bokstav i taget av det använderen skrev in
#om det är en konsontant t.ex b blir det bob. och längs till i rövarspråk strängen (som ursprungligen är tom)
# Om det inte är en konsonant, dvs vokal, läggs bokstaven till rövarspråk utan förändring

print(' Översättningen för ' + svenska.lower()+' blir: '+rövarspråk)




