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
labels_folder = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Car/Label_'
cleaned_folder = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Car/Label'
withlabel = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Car/withlabelPic'
#image_folder = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Car' 

original_files = os.listdir(cleaned_folder)

#print(original_files[10])
#print(original_files[10][:-4])

for index, file in enumerate(original_files):
	try:
		os.rename(path+'/'+file[:-4]+'.jpg', os.path.join(withlabel ,file[:-4]+'.jpg'))
	except:
		print('cannot print', file)

