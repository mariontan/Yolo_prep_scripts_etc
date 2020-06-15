# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:27:20 2020

@author: AIC-WS1
"""

#!/usr/bin/python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os

path=r'D:\Ivan\Test_data\IvanMadeDataSet\Yolo_front\front\images/'
dirs = os.listdir( path )

areaArr = []
area1 = []
area2 = []
area3 = []
area4 = []
area5 = []


def pixelPerImage():
    for item in dirs:
        if os.path.isfile(path+item):
#            print(item)
            im = Image.open(path+item)
            
            width, height = im.size
            area = width*height
            areaArr.append(area)
#            if(area<75000):
#                area1.append(area)
#            elif(area>=780000 and area<=789000):
#                area2.append(area)
#            elif(area>=75000 and area<=158000):
#                area3.append(area)
#            elif(area>=158000 and area<=300000):    
#                area4.append(area)
            if(area<=173056):
                area5.append(area)
#            else:
#                areaGreater100K.append(area)
pixelPerImage()

selectedArr =  np.array(area5)
plt.hist(selectedArr)
plt.show()
print('mean:',selectedArr.mean())
print('min:',selectedArr.min())
print('max:',selectedArr.max())
print('length: ',len(selectedArr))

