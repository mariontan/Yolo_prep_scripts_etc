# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:39:34 2020

@author: AIC-WS1
"""

import os

#path = r'D:/Ivan/Test_data/IvanMadeDataSet/Yolo_training_OID/vehicles/images'
#labels_folder = r'D:/Ivan/Test_data/DownloadedDateSets/OID/Dataset/train/Truck/YoloLabel'
#image_folder = r'D:/Ivan/Test_data/DownloadedDateSets/OID/Dataset/train/Truck' 

path = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Car'
labels_folder = r'D:/Ivan/Test_data/DownloadedDateSets/OID/Dataset/train/Car/Yolov3Label'
image_folder = r'D:/Ivan/Test_data/DownloadedDateSets/OID/Dataset/train/Car' 

files = os.listdir(path)
original_files = os.listdir(labels_folder)

#print(original_files[10])
#print(original_files[10][:-4])

for index, file in enumerate(original_files):
    #print((path+'/'+file)[:-4]+'.jpg')
    filename = (path+'/'+file)[:-4]+'.jpg'
    try:
        if os.path.isfile(filename):
            os.rename(filename, os.path.join(image_folder ,file[:-4]+'.jpg'))
    except:
        print('can not trasfer',file)
        
#os.rename(os.path.join(path, file), os.path.join(path, ''.join(['car',str(index), '.jpg'])))
    
