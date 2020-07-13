import numpy as np 
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('0001.jpg')
plt.imshow(img)
plt.show()

list_1 = []
inter1 = tuple([100, 100, 300, 250])
list_1.append(inter1)
inter1 = tuple([200, 150, 400, 300])
list_1.append(inter1)
inter1 = tuple([80, 80, 280, 230])
list_1.append(inter1)

boxes = np.array(list_1)

pos1 = np.floor(int(np.add(boxes[0][0],2)))

def _non_max_suppression_slow(boxes, overlapThresh):
	    if len(boxes) == 0:
		    return []
	    pick = []
	    x1 = boxes[:,0]
	    y1 = boxes[:,1]
	    x2 = boxes[:,2]
	    y2 = boxes[:,3]
	    area = (x2 - x1 + 1) * (y2 - y1 + 1)
	    idxs = np.argsort(y2)
	    while len(idxs) > 0:
		    last = len(idxs) - 1
		    i = idxs[last]
		    pick.append(i)
		    suppress = [last]
		    for pos in range(0, last):
			    j = idxs[pos]
			    xx1 = max(x1[i], x1[j])
			    yy1 = max(y1[i], y1[j])
			    xx2 = min(x2[i], x2[j])
			    yy2 = min(y2[i], y2[j])
			    w = max(0, xx2 - xx1 + 1)
			    h = max(0, yy2 - yy1 + 1)
			    overlap = float(w * h) / area[j]
			    if overlap > overlapThresh:
				    suppress.append(pos)
		    idxs = np.delete(idxs, suppress)
	    return boxes[pick] 

identified_patch = _non_max_suppression_slow(boxes, 0.3)  
k=1