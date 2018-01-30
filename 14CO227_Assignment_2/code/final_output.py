import cv2
import numpy as np
from matplotlib import pyplot as plt
from sys import argv

if len(argv) < 2:
    print "Usage: python %s <image>" % argv[0]
    exit()

# Entered path to the input image file
image_1 = argv[1]

img = cv2.imread(image_1)
rows,cols,ch = img.shape

pts1 = np.float32([[80.5,95],[791,131],[75,444],[791,369]])
pts2 = np.float32([[0,0],[700,0],[0,350],[700,350]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(700,350))

cv2.imwrite("output_image/stitched_rect_image.jpg", dst)
