from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np
import matplotlib.pyplot as plt
#import scipy.stats as st


def autocontrast(src_path, dst_path, white_perc, black_perc):
    img = cv2.imread(src_path)
    gray = img.sum(axis=2) // 3
    size = gray.size
    i = 255
    d = 0
    
    
    while d < white_perc and i>=0:
        where = np.where( gray == i )
        d += where[0].size/size
        i -= 1
    #p1 = st.scoreatpercentile(grey, white_perc)
    
                          
    brighest = i    
    i=0
    d=0
    
    while d < white_perc and i<=255:
        where = np.where( gray == i )
        d += where[0].size/size
        i +=1
    #p2 = st.scoreatpercentile(grey, black_perc)
    
    darkest = i
    
    for j in range(gray.shape[0]):
        for k in range (gray.shape[1]):
            if gray[j,k] > darkest and gray[j,k] < brighest :
                gray[j,k] = (gray[j,k] - darkest) * 255 / (brighest - darkest)
            else:
                if gray[j,k] > brighest :
                    gray[j,k] = 255
                else:
                    gray[j,k] = 0
    
    gray = gray.astype(np.uint8)
    cv2.imwrite(dst_path,gray)	
    #ax1.imshow(gray)
    #f.show()


if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

    assert 0 <= argv[3] < 1
    assert 0 <= argv[4] < 1

    autocontrast(*argv[1:])