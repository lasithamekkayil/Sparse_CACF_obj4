from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
img1 = cv2.imread('Family_pic.jpg')
##s = measure.compare_ssim(img1, img2, multichannel=True)
#print(s)


def _get_subwindow(init_frame, pos, window_sz):
    patch_condition =1
    init_frame = init_frame.astype(int)
    height_of_image = init_frame.shape[0]
    width_of_image = init_frame.shape[1]
    xs = np.round(pos[1]) + np.arange(0,window_sz[1],1) - np.floor(np.divide(window_sz[1],2))  
    ys = np.round(pos[0]) + np.arange(0,window_sz[0],1) - np.floor(np.divide(window_sz[0],2))
    #Checkout for out of bound corordinates, and set them to the values at the borders
    padding_left = 0
    padding_left = [padding_left+1 for xs_val in xs if xs_val<0]
    xs = [0 if xs_val<0 else xs_val for xs_val in xs]
    padding_top = 0
    if not any(xs):
        #indicates no values, dont use this patch for any calculation
        patch_condition = 0
    padding_top= [padding_top +1 for ys_val in ys if ys_val<0]
    ys = [0 if ys_val<0 else ys_val for ys_val in ys]
    if not any(ys):
        patch_condition = 0  
    padding_right = 0
    padding_right = [padding_right+1 for xs_val in xs if xs_val>width_of_image ]
    xs = [(width_of_image) if xs_val>width_of_image else xs_val for xs_val in xs]
    if not any(xs):
        patch_condition = 0
    if len(set(ys)) ==1:
        patch_condition = 0
    padding_bottom =0
    padding_bottom = [padding_bottom+1 for ys_val in ys if ys_val>height_of_image ]   
    ys = [(height_of_image) if ys_val>height_of_image else ys_val for ys_val in ys]
    if not any(ys):
        patch_condition = 0
    if len(set(ys)) ==1:
        patch_condition = 0
    xs = [int(x) for x in xs]
    ys = [int(y) for y in ys]
    height_ = window_sz[0]
    width_ = window_sz[1]
    top_left_location_y = np.floor(pos[0])-np.floor(np.divide(window_sz[0],2))
    top_left_location_x = np.floor(pos[1])-np.floor(np.divide(window_sz[1],2))
    patch_starting_point_y = ys[0]
    patch_starting_point_x = xs[0]
    patch_end_point_y = ys[len(ys)-1]
    patch_end_point_x = xs[len(xs)-1]
        
    patch = init_frame[patch_starting_point_y:patch_end_point_y, patch_starting_point_x:patch_end_point_x]            
    patch = cv2.copyMakeBorder(patch,len(padding_top), len(padding_bottom), len(padding_left), len(padding_right), cv2.BORDER_REPLICATE)
    if patch.shape[0] != window_sz[0]:
        extra_padding_bottom = window_sz[0] - patch.shape[0]
    else:
        extra_padding_bottom = 0 
    if patch.shape[1] !=window_sz[1]:
        extra_padding_right = window_sz[1] - patch.shape[1]
    else:
        extra_padding_right =0
            
    patch = cv2.copyMakeBorder(patch,0, int(extra_padding_bottom), 0, int(extra_padding_right), cv2.BORDER_REPLICATE)    
    return patch, patch_condition

patch_for_ssim = _get_subwindow(img1, [100,200], [100,200])
patch_l = patch_for_ssim[0].astype(np.uint8)
patch_for_ssim_resized = cv2.resize(patch_l, (525,525), interpolation = cv2.INTER_AREA)
s = measure.compare_ssim(np.array(patch_for_ssim_resized), np.array(patch_for_ssim_resized), multichannel=True)
print(s)
K=1