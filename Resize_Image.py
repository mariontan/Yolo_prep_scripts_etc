# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:27:20 2020

@author: AIC-WS1
"""

#!/usr/bin/python
from PIL import Image
import os, sys

#path = r"D:/Ivan/Test_data/Stanford_AI_cars_modified/train/motorcycle/"
path = r"D:/Ivan/Test_data/Truck_Google_search/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            print(item)
            f, e = os.path.splitext(path+'/resized/'+item)
            imResize = im.resize((352,352), Image.ANTIALIAS).convert('RGB')
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()