from os import listdir
from random import shuffle, random

if __name__ == "__main__":
    ruta="./Annotations"
    lista=[]

    test_prop=0.2

    for name in listdir(ruta):
        name_splited=name.split(".")

        if ( name_splited[len(name_splited)-1]=="xml"):
            #rename
            
            save=name_splited[0]
            lista.append(save)


              
                
    f=open("train.txt","w+")
    f2=open("test.txt","w+")
    count=[0,0,0,0,0]
    indice=0
    corte=2150
    train_n=0.8
    shuffle(lista)
    lista_test=[]
    for name in lista:

        if random()<test_prop:
            f2.write(name+'\n')
        else:
            f.write(name+'\n')

    f.close()
    f2.close()
    print("Done!")
    print (count)
