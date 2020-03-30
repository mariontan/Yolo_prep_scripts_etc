# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:27:20 2020

@author: AIC-WS1
"""

#!/usr/bin/python
from PIL import Image
import os, sys

#path = r"D:/Ivan/Test_data/Stanford_AI_cars_modified/train/motorcycle/"
#path = r"D:\Ivan\Test_data\IvanMadeDataSet\Yolo_Cars_Front_SlightSide_View\extraImages\cars"
path = r"D:/Ivan/Test_data/IvanMadeDataSet/Stanford_AI_cars_modified/test/buses/"
dirs = os.listdir( path )

#aspect ratio width:height
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            width, height = im.size
            if width > 600 or height > 600:
                aspectRatio = width/height
                width = 600
#                print(aspectRatio)
#                print(width)
#                print(300/aspectRatio)
            
            f, e = os.path.splitext(path+'/resized/'+item)
            imResize = im.resize((width,int(width/aspectRatio)), Image.ANTIALIAS).convert('RGB')
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()