from os import listdir
from random import shuffle, random

if __name__ == "__main__":
    path="./Annotations_classes"
    images=[]

    test_prop=0.2

    train=open("trainval.txt","w+")
    test=open("test.txt","w+")
    count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    c=-1
    for label in listdir(path):
        train_class=label+"_trainval.txt"
        test_class=label+"_test.txt"
        train_i=open(train_class,"w+")
        test_i=open(test_class,"w+")
        new_path = path+"/"+label
        c+=1

        for name in listdir(new_path):
            name_splited=name.split(".")


            if ( name_splited[len(name_splited)-1]=="xml"):
                #rename
                
                select=random()            
                save=name_splited[0]


                if select<test_prop:
                    test_i.write(save+'\n')
                    test.write(save+'\n')
                    count[c]+=1

                else:
                    train_i.write(save+'\n')
                    train.write(save+'\n')

        train_i.close()
        test_i.close()

    train.close()
    test.close()
          
    print("Done!")
    print (count)
