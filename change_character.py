
	
import os
#path = r'D:/Ivan/Test_data/YoloV3_Data/newlabels/truck'
path = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_3k_2\newlabels\1'
files = os.listdir(path)


for index, file in enumerate(files):
#    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['',str(index), '.jpg'])))
    labels = []
    with open(os.path.join(path, file)) as f:
        lines = f.readlines()
    
    for line in lines:
        labels.append(line.replace('Truck','1'))
    
    print(lines) # ["This is the line that's replaced.\n", 'This is the second line.\n']
    with open(os.path.join(path, file), "w") as f:
        f.writelines("".join(labels))
    f.close()
    
'''
>>> s = list("Hello zorld")
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'z', 'o', 'r', 'l', 'd']
>>> s[6] = 'W'
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
>>> "".join(s)
'Hello World'
'''