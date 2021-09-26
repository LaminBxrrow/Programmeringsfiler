from os import remove

def meningsräknare(filnamn):
    with open(filnamn+'.txt','r',encoding="utf-8") as file:
        hello=file.read()
        putsad_fil=hello.replace('\n',' ')
        sterilseradfil=putsad_fil.strip()
        lista_ord=sterilseradfil.split(' ')
        lista_mening=sterilseradfil.split('.')

        lista_mening.remove(lista_mening[len(lista_mening) - 1])

    return len(lista_ord),len(lista_mening)

def main():

    ord,meningar=meningsräknare('idas')
    print(ord,meningar)

main()