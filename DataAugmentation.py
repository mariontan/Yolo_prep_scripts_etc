# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:17:35 2020

@author: AIC-WS1
"""

import os
from PIL import Image
import numpy as np
from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2 

path = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_Data_Augmentation/'
path_label = path + 'convertedYolov3Label/'
path_image = path + 'image/'
files = os.listdir(path_label)


def scale(path_image,path_label,file,img,label):
    img_, bboxes_ = RandomScale(0.3, diff = True)(img.copy(), label.copy())
    np.savetxt(path_label+'scaled'+file[:-4]+'.txt',bboxes_, delimiter=' ', fmt='%f')
    im = Image.fromarray(img_)
    im.save((path_image+'scaled'+file[:-4]+'.jpg'))

def loadFile(path_image,path_label,folder):
    dataAugmentFolder = path+folder 
    if not os.path.exists(dataAugmentFolder):
        os.mkdir(dataAugmentFolder)
    
    if not os.path.exists(dataAugmentFolder+'image/'):
        os.mkdir(dataAugmentFolder+'image/')
        
    if not os.path.exists(dataAugmentFolder+'label/'):
        os.mkdir(dataAugmentFolder+'label/')
        
    for file in files:
        img = cv2.imread(path_image+file[:-4]+'.jpg')[:,:,::-1]
        label = np.array([[0,0,0,0,0]])
        with open(path_label+file[:-4]+'.txt') as f:
            lines = f.readlines()
            for line in lines:
                label = np.append(label,[np.fromstring(line, dtype=float, sep= ' ')],axis = 0)
        label = label[1:]
        scale(dataAugmentFolder+'image/',dataAugmentFolder+'label/',file,img,label)

loadFile(path_image,path_label,'scaledFront/')