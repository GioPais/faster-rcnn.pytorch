from os import listdir, makedirs
import os
import glob, shutil
from random import shuffle, random

if __name__ == "__main__":
    PATH=os.getcwd()
    annots_path="./Annotations_classes"
    images_path="./JPEGImages_classes"
    annots_dest="./Annotations"
    images_dest="./JPEGImages"
    sets_path="ImageSets/Main/"

    test_prop=0.2
    os.system("mkdir ImageSets")
    os.system("mkdir ImageSets/Main")
    train=open(sets_path+"trainval.txt","w+")
    test=open(sets_path+"test.txt","w+")
    count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    idx=-1
    os.system("mkdir JPEGImages")
    os.system("mkdir Annotations")
    for label in listdir(annots_path):
        train_class=sets_path+label+"_trainval.txt"
        test_class=sets_path+label+"_test.txt"
        train_i=open(train_class,"w+")
        test_i=open(test_class,"w+")
        new_annots_path = annots_path+"/"+label
        idx+=1

        files_list=listdir(new_annots_path)
        shuffle(files_list)
        print(label)
        counter=0
        for name in files_list:
            name_splited=name.split(".")
            counter+=1

            if ( name_splited[len(name_splited)-1]=="xml"):
                #rename
                save=name_splited[0]
                if counter<=test_prop*len(files_list):
                    test_i.write(save+'\n')
                    test.write(save+'\n')
                    count[idx]+=1

                else:
                    train_i.write(save+'\n')
                    train.write(save+'\n')

        train_i.close()
        test_i.close()
        command="find "+images_path+"/"+label+" -type f -print0 | xargs -0 mv -t "+images_dest
        os.system(command)

        command="find "+annots_path+"/"+label+" -type f -print0 | xargs -0 mv -t "+annots_dest
        os.system(command)
        
    os.system("rm -r "+images_path)
    os.system("rm -r "+annots_path)

    train.close()
    test.close()
          
    print("Done!")
    print (count)
