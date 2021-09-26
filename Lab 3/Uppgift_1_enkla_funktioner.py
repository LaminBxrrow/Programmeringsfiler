''' Skriven av : Lamin Barrow
17/09.-21'''

def torrhumor():
    print('Det viktigaste när du köper fotbollsskor är att de passar bra!')

def uppmuntran():
    print('Om du misslyckas med plan A, glöm inte att det finns 27 andra bokstäver i alfabetet!')

def responsgivande():
    skamt_humor=input('Vill du ha ha uppmuntran ELLER humor?: ')
    if skamt_humor.lower()=='uppmuntran':
        uppmuntran()
    else: torrhumor()

responsgivande()
