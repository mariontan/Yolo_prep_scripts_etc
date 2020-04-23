# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:34:22 2020

@author: AIC-WS1
"""

import os
import numpy as np
import cv2 

path = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_Data_Augmentation/'
path_label = path + 'label/'
path_image = path + 'image/'
files = os.listdir(path_label)

def convertYolov3Label(path_image,path_label,file,folder):
    img = cv2.imread(path_image+file[:-4]+'.jpg')[:,:,::-1]
    Y, X, _ = img.shape
    label = np.array([[0,0,0,0,0]])
    with open(path_label+file[:-4]+'.txt') as f:
        lines = f.readlines()
        for line in lines:
                line = line[:-2].split(' ')
                x_1 = (float(line[1])*X)-((float(line[3])*X)/2)
                y_1 = (float(line[2])*Y)-((float(line[4])*Y)/2)
                x_2 = (float(line[1])*X)+((float(line[3])*X)/2)
                y_2 = (float(line[2])*Y)+((float(line[4])*Y)/2)
                cls = 1
                label = np.append(label,[[x_1,y_1,x_2,y_2,cls]],axis = 0)
    np.savetxt(folder+file[:-4]+'.txt',label[1:], delimiter=' ', fmt='%f')
    
folder = path+'convertedYolov3Label/'
if not os.path.exists(folder):
    os.mkdir(folder)
for file in files:
    convertYolov3Label(path_image,path_label,file,folder)