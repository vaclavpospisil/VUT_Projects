import cv2
import numpy as np
from matplotlib import pyplot as plt
import skimage
from skimage import exposure
from os import listdir
from os.path import join

fpath = 'C:\\Users\\Venca\\downloads\\VSC_projekt\\'
cvfiles = [join(fpath, directory) for directory in listdir(fpath)]

for path in cvfiles:
    img = cv2.imread(path, 0)
    gamma_corrected = exposure.adjust_gamma(img, 1.8)       #
    log_corrected = exposure.adjust_log(gamma_corrected, 2) # na riadenie kontrastu a brightness
    img = log_corrected

    ksize = 69
    median_filter = cv2.medianBlur(img, ksize)
    img = median_filter

    ret,thresh5 = cv2.threshold(img,80,255,cv2.THRESH_TOZERO_INV)
    img = thresh5


    scale_factor = 10000
    # create a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[200:700, 200:800] = 255
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    # Calculate histogram with mask and without mask
    hist_full1 = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist_mask1 = cv2.calcHist([img], [0], mask, [256], [0, 256])
    hist_concat = hist_full1[2:]
    hist_mask_concat = hist_mask1[2:]

    white_vals = hist_concat[0]
    if white_vals != [0.]:
        eval = 'POSITIVE on contamination'
    else:
        eval = 'NEGATIVE on contamination'

    print (white_vals)
    print ('Evaluation of the product:', eval)

    plt.figure()
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    #plt.subplot(224), plt.plot(hist_full1/scale_factor, color='r'), plt.plot(hist_mask1/scale_factor, color='g')
    plt.subplot(224), plt.plot(hist_concat, color='r')#, plt.plot(hist_mask_concat, color='g')
    #plt.xlim([0, 256])
    plt.xlim([-10, 256])
    #plt.ylim([0,100])
    plt.grid()

    plt.show()

    




