from os import listdir, makedirs
import os
import glob, shutil
from random import shuffle, random

if __name__ == "__main__":
    image_path="./Images_raw"
    image_dest="./JPEGImages_classes"
    annots_path="./Annotations_raw"
    annots_dest="./Annotations_classes"

    
    os.system("mkdir JPEGImages_classes")
    os.system("mkdir Annotations_classes")
    for label in listdir(image_path):
        new_image_path = image_path+"/"+label
        print(new_image_path)
        command="find "+image_path+"/"+label+" -type f -print0 | xargs -0 mv -t "+image_dest+"/"+label
        os.system("mkdir ./JPEGImages_classes/"+label)
        os.system(command)
        

        new_annots_path = annots_path+"/"+label
        print(new_annots_path)
        command="find "+annots_path+"/"+label+" -type f -print0 | xargs -0 mv -t "+annots_dest+"/"+label
        os.system("mkdir ./Annotations_classes/"+label)
        os.system(command)
        
    os.system("rm -r "+image_path)
    os.system("rm -r "+annots_path)
        
          
    print("Done!")
