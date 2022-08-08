from copy import copy
import shutil
import os

from isort import file



#onedrive kbase path
onedrive='C:\\Users\\mmak\\OneDrive - CMHC-SCHL\\Calgary\\'

kbase_dir = '.\\kbase\\'
pareto_dir = '.\\data\\pareto\\'
resales_dir='.\\data\\resales\\'

def copy_from_dir(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root,filename)
            if file_path[-2:] != 'h5':
                
                print(file_path)
                print(root)
                print(os.path.join(onedrive,file_path))
                output_path = os.path.join(onedrive,file_path)
                shutil.copy2(file_path,output_path)


copy_from_dir(kbase_dir)
copy_from_dir(pareto_dir)
copy_from_dir(resales_dir)


            
