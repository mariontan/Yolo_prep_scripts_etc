
	
import os
path = r'D:\Ivan\Test_data\IvanMadeDataSet\Yolo_Cars_Front_SlightSide_View\train\1'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['car',str(index), '.jpg'])))