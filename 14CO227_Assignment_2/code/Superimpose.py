import cv2
import numpy as np
from matplotlib import pyplot as plt
from sys import argv

if len(argv) < 3:
    print "Usage: python %s <image> <image>" % argv[0]
    exit()

# Entered path to the input image file
image_1 = argv[1]

img = cv2.imread(image_1)

image_2 = argv[2]

img1 = cv2.imread(image_2)

k=0
i=3



''' Gaussian Blur '''


blur_1 = cv2.GaussianBlur(img,(i,i),k)
Image_1 = "image_1.side."+str(i)+".std."+str(k)+".JPG"
cv2.imwrite(Image_1,blur_1)
blur_2 = cv2.GaussianBlur(img1,(i+2,i+2),k)
Image_2 = "image_2.side."+str(i)+".std."+str(k)+".JPG"
cv2.imwrite(Image_2,blur_2)


threshold_1 = 0.03
threshold_2 = 0.03



''' Image 1 ---> Harris Corner Detection '''



gray_1 = cv2.cvtColor(blur_1,cv2.COLOR_BGR2GRAY)
gray_1 = np.float32(gray_1)
dst_1 = cv2.cornerHarris(gray_1,2,3,0.04)


#result is dilated for marking the corners, not important
dst_1 = cv2.dilate(dst_1,None)

ret, dst = cv2.threshold(dst_1,0.01*dst_1.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray_1,np.float32(centroids),(5,5),(-1,-1),criteria)
results1 = open('image1_corners.txt','w')
#results1.write(str(corners)+'\n')
for i in range(len(corners)):
    results1.write(str(corners[i][0])+' '+str(corners[i][1])+'\n')
#print(len(corners))


img[dst_1>threshold_1*dst_1.max()]=[0,0,255]
Image_1 = "image_1.threshold_"+str(threshold_1)+".jpg"
cv2.imwrite(Image_1,img)




'''Image 2 ---> Harris Corner Detection'''


gray_2 = cv2.cvtColor(blur_2,cv2.COLOR_BGR2GRAY)
gray_2 = np.float32(gray_2)
dst_2 = cv2.cornerHarris(gray_2,2,3,0.04)
#result is dilated for marking the corners, not important
dst_2 = cv2.dilate(dst_2,None)

ret, dst = cv2.threshold(dst_2,0.01*dst_2.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners1 = cv2.cornerSubPix(gray_2,np.float32(centroids),(5,5),(-1,-1),criteria)
#print(len(corners))
results2 = open('image2_corners.txt','w')
for i in range(len(corners1)):
    results2.write(str(corners1[i][0])+' '+str(corners1[i][1])+'\n')
# Now draw them

img1[dst_2>threshold_2*dst_2.max()]=[0,0,255]
Image_2 = "image_2.threshold_"+str(threshold_2)+".jpg"
cv2.imwrite(Image_2,img1)

results1.close()
results2.close()

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

plt.imshow(img1)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
