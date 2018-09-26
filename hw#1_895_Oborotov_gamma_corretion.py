from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np
import matplotlib.pyplot as plt


def gamma_correction(src_path, dst_path, a, b):
    img = cv2.imread(src_path)
    f , ax1 = plt.subplots(1, 1)
    
    for i in range(img.shape[0]):
        
        for j in range(img.shape[1]):
            
            for k in range(img.shape[2]):
                
                img[i,j,k] = (img[i,j,k]/255)**b*a
    
    cv2.imwrite(dst_path,img)
    #ax1.imshow(img)
    #f.show()


if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

    gamma_correction(*argv[1:])
