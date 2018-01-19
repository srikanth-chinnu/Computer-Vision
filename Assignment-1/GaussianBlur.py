import cv2
import numpy as np
from sys import argv

if len(argv) < 2:
    print "Usage: python %s <image>" % argv[0]
    exit()

# Entered path to the input image file
filename = argv[1]

results = open('GB_Results.txt','w')

img = cv2.imread(filename)

k=0
'''
I'm taking a square kernel, so height = width = i
i values ranges from 3-50,every alternate odd number.
with standard deviation (k) range as 0-5 same along x and y axes.
'''

while(k<=5):
	i=3
	while(i<=50):
		blur = cv2.GaussianBlur(img,(i,i),k)
		Filename = "img.side."+str(i)+".std."+str(k)+".jpg"
		cv2.imwrite("GaussianBlur/"+Filename,blur)
		output = Filename+" is a GaussianBlur output image of "+filename+" with standard deviation "+str(k)+" and square kernel side length "+str(i)+"\n"
		results.write(output)
		i+=4
	k+=1

results.close()
