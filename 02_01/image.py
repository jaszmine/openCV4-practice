import numpy as np
import cv2

# function used to read in images
img = cv2.imread('../images/devon.jpg')

# checking type
#print(type(img))
# in terminal: `python image.py`
# output: <class 'numypy.ndarray'>

# confirms if image has been read
#print(img.shape)
# output: (360, 480, 3)
# means image has 360 rows, 480 cols, & 3 channels (corresponding to BGR)

# all rows, all cols, 1st channel in BGR (B)
b = img[:,:,0]
print(b)
# returns values of numpy array

g = img[:,:,1]
r = img[:,:,2]

# displays image - name of window, var being displayed

cv2.imshow('Blue', b)
cv2.imshow('Gree', g)
cv2.imshow('Red', r)
# returns 3 intensity/grayscale channels representing the colors
# larger light contributions are appear lighter

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()