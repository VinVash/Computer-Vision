import numpy as np
import cv2

# Storing the original image in the variable called img1.
img1 = cv2.imread('checkpoint2.png')

# b, g, r = (img1[300, 300])


# x1 = [0, 0, 0] because we have to convert all the circles in white colour before moving on. Hence, all colours
# except white are passed in the inRange function.
x1 = [0, 0, 0]
small = np.array(x1)

x2 = [254, 254, 254]
large = np.array(x2)

# Applying mask through the inRange function, which converts the image into a black and white image. The image is
# converted into white where the colour is in the range specified and black where the colour is not in the range
# specified.
masker = cv2.inRange(img1, small, large)
# Applying mask on the original image.
res = cv2.bitwise_and(img1, img1, mask=masker)

# Storing the masked image with the name 'checkpoint2_black.png'.
cv2.imwrite('checkpoint2_black.png', res)

# Reading the masked image in the variable img.
img = cv2.imread('checkpoint2_black.png')

# Copying the masked image in the variable output.
output = img.copy()

# Converting the masked image into grayscale image.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blurring the grayscale image.
gray_blurred = cv2.medianBlur(gray, 5)

# Applying HoughCircles function to store the circles detected in an array.
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=4, minRadius=0, maxRadius=500)

# Creating a list and storing the array elements in the list for easy access to the value of the radius.
l = []
l = circles.tolist()
# print(l)   Making sure the list contains the circles.

# Initialising the max radius first to zero and storing it in a variable 'ans'.
ans = 0

for j in range(0, 5):
    if int(l[0][j][2]) > ans:
        ans = int(l[0][j][2])
        # Updating the max radius.
        # print(ans) Making sure the max radius is present in the 'ans' variable.

for k in range(0, 5):
    if int(l[0][k][2]) == ans: # Checking whether the current radius equals max radius
        # print(ans) Making sure that 'ans' contains the max radius, i.e., 114.
        # Drawing circles on the original image, i.e., img1.
        cv2.circle(img1, (int(l[0][k][0]), int(l[0][k][1])), ans, (0, 0, 0), 5) # Highlighting the biggest circle in
        # the original image, i.e., img1.

cv2.imshow('result', img1) # Displaying the result, i.e., the biggest circle highlighted in the image.
cv2.waitKey(0)
cv2.destroyAllWindows()
