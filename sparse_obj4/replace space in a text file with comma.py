#replace space in a text file with comma
import numpy as np
import os 
#Get the current path
cwd = os.getcwd()
k =[]
#f=open(os.path.join('datasets/Biker/', 'groundtruth_rect.txt'))
hello=open(os.path.join('datasets/Vase/', 'groundtruth_rect_actual.txt'))
for i in hello:
    j = i.replace('\t',',')
    m = j.replace('\n','')
    k.append(m)
updated_groundtruth = list(k)
#with open("updated_groundtruth.txt", "w") as output:
    #output.write(str(updated_groundtruth))
with open("datasets/Vase/groundtruth_rect.txt", 'w') as output:
    for row in updated_groundtruth:
        output.write(str(row) + '\n')