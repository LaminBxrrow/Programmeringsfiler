#Skrivet av Lamin Barrow
# 17/09-21

def ge_mig_ett_heltal():
    try:
        intervall_heltal=[1,2,3,4,5,6,7,8,9,10]
        givet_heltal = int(input('Skriv ett heltal inom intervallet 1-10: '))
        while givet_heltal not in intervall_heltal:
            givet_heltal = int(input('Skriv ett heltal inom intervallet 1-10: '))
        return givet_heltal
    except ValueError:
        print('Du måste ange en siffra!')

ok_svar=(ge_mig_ett_heltal())
print(ok_svar)