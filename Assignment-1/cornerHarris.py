import cv2
import numpy as np
from sys import argv

if len(argv) < 2:
    print "Usage: python %s <image>" % argv[0]
    exit()

# Entered path to the input image file
filename = argv[1]

results = open('HCD_Results.txt','w')

# Threshold for an optimal value, it may vary depending on the image.
threshold = 0.02
while(threshold<=0.2):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    img[dst>threshold*dst.max()]=[0,0,255]
    Filename = "img.threshold_"+str(threshold)+".jpg"
    cv2.imwrite("cornerHarris/"+Filename,img)
    output = Filename+" is a Harris Corner Detector output image of "+filename+" with threshold "+str(threshold)+"\n"
    results.write(output)
    threshold += 0.01

results.close()
#cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
