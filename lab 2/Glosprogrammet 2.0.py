from _ast import While
# Rovarspråk av Lamin Barrow
# Skrivet den 12/9-2021
print("välkommen till glosprogrammet!")
print((""))

glossary_Sv=['Orubblig','Blygsam','Glad','Busig','Tam','Fräck']
glossary_Eng=['adamant','modest','jolly','impish','docile','sassy']
# två listor som innehåller svenska respektive engelska orden (glosparen)

amount_correct=0
for i in range(len(glossary_Eng)):
       answer= input('Vad är den svenska översättningen för ordet '+glossary_Eng[i] + ':? ')
       if answer.capitalize()==glossary_Sv[i]:
               amount_correct+=1
#for slingan kommer att kontrollera ett ord i taget, om svaret är lika med det svenska ordet
#med samma indexplats kommer man få en poäng, som lagras i variable amount_correct

if amount_correct==6:
        print('Perfekt, du översatte alla 6 glosor korrekt!!!')
if amount_correct == 5:
            print('Dem här orden kan du nästan! , du 5 av 6 glosor korrekt!')
if amount_correct==4:
        print('Bra, du 4 av 6 glosor korrekt.')
if amount_correct<4:
        print('Aj då, du översatte endast '+ str(amount_correct) +' glosor korrekt.')

#valde att göra det lite mer"detaljerat" än att bara ange hur många rätt man fick


