import os
#path = r'D:/Ivan/Test_data/YoloV3_Data/newlabels_Copy/3'
path = r'D:/Ivan/Test_data/YoloV3_Data/newlabels/truck'
files = os.listdir(path)


for index, file in enumerate(files):
#    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['',str(index), '.jpg'])))

    with open(os.path.join(path, file)) as f:
        lines = f.readlines()
    
    print(lines)
    lines=list(lines[0])
    #print(lines) # ["This is the line that's replaced.\n", 'This is the second line.\n']
    lines[0] = '1'
    print("".join(lines))
    with open(os.path.join(path, file), "w") as f:
        f.writelines("".join(lines))
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