#Markos film
from random import *


def bubblesorterare(lista):

    print('Ordnad lista',lista)
    shuffle(lista)
    print('Blandad lista',lista)

    for i in range(len(lista)):
        minsta_elementet = lista[i]
        elementets_plats = i
        position = i

        for j in range(position + 1, len(lista)):
            if lista[j] < minsta_elementet:
                elementets_plats = j
                position = lista[j]
                lista[elementets_plats] = lista[position]
                lista[position] = minsta_elementet


    return lista

print(bubblesorterare([10,7]))



#blandad_lista[elementets_plats] = blandad_lista[position]
   # print("Sorterade element: " + str(sorterat))
    #print("Mina element på plats: " + str(e) + "\n")
    #visa_list(start)
    #print("Flyttar från stället min ska in till stället min ska från.")
    #start[pos] = min
    #print("lagt in minsta elementet på rätt plats")
    #visa_list(start)
    #input("Tryck enter för nästa steg")


