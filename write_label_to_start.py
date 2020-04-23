# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:14:09 2020

@author: AIC-WS1
"""

import os

path = r'D:\Ivan\Developer\OIDv4_ToolKit-master\OID\Dataset\train\Truck\Label/'
files = os.listdir(path)


for file in files:
    labels = []
    with open(path+file) as f:
        lines = f.readlines()
    for line in lines:
        label = line.replace(' 1.000000','')
        labels.append('1 '+label)
        print('1 '+label)
    with open(path+file, "w") as f:
        f.writelines("".join(labels))
    f.close()
