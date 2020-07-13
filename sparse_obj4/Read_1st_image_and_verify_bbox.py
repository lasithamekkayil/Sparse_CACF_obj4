#Read 1st image from dataset and keep bounding box on image
import numpy as np 
import os
import cv2

dataset1 = 'Liquor'
img_path = 'F:/current_code_15_06_202/datasets/'+ dataset1 

frame_list = []
for frame in os.listdir(img_path):
    if os.path.splitext(frame)[1] == '.jpg':
        frame_list.append(os.path.join(img_path, frame))

groundtruth = 'F:/current_code_15_06_202/datasets/groundtruth_rect.txt'

f=open(os.path.join('datasets/'+ dataset1, 'groundtruth_rect.txt'))
#Convert the text file to a list
gt = []
for line in f:
    stripped_line = line. strip()
    line_list = stripped_line. split(',')
    gt. append(line_list)
f. close()  
#Convert the strings in the text file to a list
for j in range(len(gt)):
    temp = gt[j]
    for i in range(0, len(temp)): 
        temp[i] = int(temp[i])
    gt[j] = temp   

color = (255, 0, 0)
thickness = 2
for idx in range(0, len(frame_list)):
    current_frame = cv2.imread(frame_list[idx])
    cv2.rectangle(current_frame, (256,152), (256+73,152+210), color, thickness) 
    cv2.imshow('demo', current_frame)
    cv2.waitKey(100)
