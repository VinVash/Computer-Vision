import cv2
import numpy as np

img1 = cv2.imread('checkpoint2.png')

# b, g, r = (img1[300, 300])
# print(b)
# print(g)      First print the rgb values of the green colour, which we have to pass in the following command:
# print(r)

# x1 = [76, 177, 34] are the BGR values of the green colour which we have to keep in the picture.
x1 = [76, 177, 34]
small = np.array(x1)

x2 = [254, 254, 254]
large = np.array(x2)

masker = cv2.inRange(img1, small, large)
res = cv2.bitwise_and(img1, img1, mask=masker) # Masking the image with the colour decided.

cv2.imwrite('checkpoint2_black.png', res) # Storing the masked image with the name 'checkpoint2_black.png'.

img = cv2.imread('checkpoint2_black.png') # Reading the image 'checkpoint2_black.png' in the variable 'img'.
output = img.copy() # Storing a copy of the image in the variable 'output'.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting the masked image into grayscale.

gray_blurred = cv2.medianBlur(gray, 5) # Blurring the image.

# Using the HoughCircles function to store the detected circles in the blurred image.
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=4, minRadius=0, maxRadius=500)

# Making a list which contains the array elements of circles array.
l = []
l = circles.tolist()
print(l)

# for i in range(0, 3):
    # print(l[0][i][0])       # Checking that the co-ordinates of the circles are present in the list.
    # print(l[0][i][1])

# Joining the centers of the first two circles through a black line in the original image.
img1 = cv2.line(img1, (int(l[0][0][0]), int(l[0][0][1])), (int(l[0][1][0]), int(l[0][1][1])), (0, 0, 0), 5)

# Joining the centers of the next two circles through a black line in the original image.
img1 = cv2.line(img1, (int(l[0][1][0]), int(l[0][1][1])), (int(l[0][2][0]), int(l[0][2][1])), (0, 0, 0), 5)
# img1 = cv2.line(img1, (int(l[0][2][0]), int(l[0][2][1])), (int(l[0][0][0]), int(l[0][0][1])), (0, 0, 0), 5)

# Displaying the original image with the connected circles.
cv2.imshow('output', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
