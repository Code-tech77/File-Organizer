#importation 
import os 
import shutil

#user interaction
path = input("Enter Folder Path: ")
files = os.listdir(path)

#The main proccess
for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1: ]
    
    #if & Else Statment
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        
        
    
    