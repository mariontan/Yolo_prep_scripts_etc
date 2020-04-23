# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:39:34 2020

@author: AIC-WS1
"""

import os

path = r'D:/Ivan/Developer/OIDv4_ToolKit-master/OID/Dataset/train/Truck'
path_YoloLabel = path + '/Yolov3Label'
files = os.listdir(path)

if not os.path.exists(path_YoloLabel):
    os.mkdir(path_YoloLabel)

for index, file in enumerate(files):
    if file.endswith('.txt'):
        os.rename(os.path.join(path, file), os.path.join(path_YoloLabel ,file))
    
