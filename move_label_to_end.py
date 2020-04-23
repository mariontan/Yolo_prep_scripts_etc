import os

path = r'D:\Ivan\Test_data\IvanMadeDataSet\OID_Truck_Data_Augmentation/'
path_label = path + 'label/'
path_image = path + 'image/'
files = os.listdir(path_label)


for file in files:
    labels = []
    with open(path_label+file) as f:
        lines = f.readlines()
    for line in lines:
        label = line.replace('Truck ','')
        labels.append(label[:-2]+ ' 1\n')
    print(labels)
    with open(path_label+file, "w") as f:
        f.writelines("".join(labels))
    f.close()
