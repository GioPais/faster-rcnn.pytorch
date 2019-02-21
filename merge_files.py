from os import listdir, makedirs
import os
import glob, shutil
from random import shuffle, random

if __name__ == "__main__":
    path="./Images"
    dest="./JPEGImages"
    images=[]

    
    os.system("mkdir JPEGImages")
    for label in listdir(path):
        new_path = path+"/"+label
        print(new_path)
        command="find "+path+"/"+label+" -type f -print0 | xargs -0 mv -t "+dest+"/"+label
        os.system("mkdir ./JPEGImages/"+label)
        os.system(command)
        
        
          
    print("Done!")
