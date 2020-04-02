# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:09:12 2020

@author: Ivan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:39:34 2020
@author: AIC-WS1
"""

import os
import pandas as pd
import shutil
import re 

viewType = './left.txt'
foldername = re.search('./(.+?).txt',viewType).group(1)
imageFolder = './forboxing/0/'
labelsFolder = './newlabels/0/'

if not os.path.exists('./'+foldername):
    os.mkdir('./'+foldername)

if not os.path.exists('./'+foldername+'/yoloV3Labels'):
    os.mkdir('./'+foldername+'/yoloV3Labels')

df = pd.read_csv(viewType,sep = ',',header=None)
filenames = df[1].values

for filename in filenames:
    shutil.copyfile(imageFolder+filename+'.jpg',
                    foldername+'/'+filename+'.jpg')
    shutil.copyfile(labelsFolder+filename+'.txt',
                    foldername+'/yoloV3Labels/'+filename+'.txt')
