# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:13:34 2020

@author: AIC-WS1
"""

import glob
import os
import numpy as np
import sys
#current_dir = "./data/artifacts/images"
current_dir = r'D:/Ivan/Test_data/YoloV3_Data/Yolo_training/vehicles/images'
split_pct = 10  # 10% validation set
file_train = open(r"D:/Ivan/Test_data/YoloV3_Data/Yolo_training/vehicles/train.txt", "w")  
file_val = open(r"D:/Ivan/Test_data/YoloV3_Data/Yolo_training/vehicles/val.txt", "w")  
counter = 1  
index_test = round(100 / split_pct)  
for fullpath in glob.iglob(os.path.join(current_dir, "*.JPG")):  
  title, ext = os.path.splitext(os.path.basename(fullpath))
  if counter == index_test:
    counter = 1
    file_val.write(current_dir + "/" + title + '.jpg' + "\n")
  else:
    file_train.write(current_dir + "/" + title + '.jpg' + "\n")
    counter = counter + 1
file_train.close()
file_val.close()