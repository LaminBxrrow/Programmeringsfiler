#kommentarer
import os

def f1(filnamn):
    path='C:\\Users\\Lamin Barrow\Downloads\\'+filnamn+'.txt'
    list=[]
    if os.path.exists(path):
        with open(filnamn+'.txt','r',encoding="utf-8") as file:
            for line in file:
                cleanmaster=line.split('\n')
                list.append(cleanmaster)

    else:
        print('There is no text-file named '+ filnamn)

    return list
print((f1('idas')))
