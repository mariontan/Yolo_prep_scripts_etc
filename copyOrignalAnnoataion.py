# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:40:09 2020

@author: AIC-WS1
"""

import os
from shutil import copyfile

path = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_Data_Augmentation/image'
labelFolder = 'D:\Ivan\Test_data\DownloadedDateSets\OID_truck_3k_4\combinedVOCLabels'
destFolder = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_Data_Augmentation/label'

files = os.listdir(path)

for file in files:
    try:
        copyfile(labelFolder+'/'+file[:-4]+'.txt',destFolder+'/'+file[:-4]+'.txt')
    except:
        pass
    