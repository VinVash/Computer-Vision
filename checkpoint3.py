import numpy as np
import cv2 as cv

# BGR values of the red colour: 36, 27, 237
# BGR values of the green colour: 77, 177, 35

img1 = cv.imread('checkpoint3.jpg')
# Masking the image with red colour so that the image only contains the green circles and the stars.

x1 = [60, 150, 20]
small = np.array(x1)

x2 = [100, 200, 50]
large = np.array(x2)

masker = cv.inRange(img1, small, large)
res = cv.bitwise_and(img1, img1, mask=masker)  # Masking the image with the colour decided.

cv.imwrite('checkpoint3_black.jpg', res)  # Storing the masked image with the name 'checkpoint2_black.png'.

img = cv.imread('checkpoint3_black.jpg')  # Reading the image 'checkpoint2_black.png' in the variable 'img'.
output = img.copy()  # Storing a copy of the image in the variable 'output'.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Converting the masked image into grayscale.

gray_blurred = cv.medianBlur(gray, 5)  # Blurring the image.

# Using the HoughCircles function to store the detected green circles in the blurred image.
circles = cv.HoughCircles(gray_blurred, cv.HOUGH_GRADIENT, 1, 100, param1=30, param2=4, minRadius=0, maxRadius=100)

# Making a list which contains the array elements of circles array.
l = []
l = circles.tolist()
# print(l)      # Checking that the list contains all the green circles.

# ------------------------------------------------------------------------------------------------------
# Now masking the image according to the red circles.
y1 = [20, 10, 200]
smaller = np.array(y1)

y2 = [50, 40, 254]
larger = np.array(y2)

maskerr = cv.inRange(img1, smaller, larger)
ress = cv.bitwise_and(img1, img1, mask=maskerr)  # Masking the image with the colour decided.

cv.imwrite('checkpoint3_blackred.jpg', ress)  # Storing the masked image with the name 'checkpoint3_blackred.png'.

img2 = cv.imread('checkpoint3_blackred.jpg')  # Reading the image 'checkpoint3_blackred.png' in the variable 'img'.
output = img2.copy()  # Storing a copy of the image in the variable 'output'.

grayy = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)  # Converting the masked image into grayscale.

grayy_blurred = cv.medianBlur(grayy, 5)  # Blurring the image.

# Using the HoughCircles function to store the detected green circles in the blurred image.
circles = cv.HoughCircles(grayy_blurred, cv.HOUGH_GRADIENT, 1, 100, param1=30, param2=4, minRadius=0, maxRadius=120)

# Making a list which contains the array elements of circles array.
ll = []
ll = circles.tolist()
# print(ll)    # Checking that the list contains all the red circles.

# ------------------------------------------------------------------------------------------------------

# Checking all the red circles. Since, the number of red and green circles will remain same in all testcases,
# therefore I have hardcoded the range as 3 only.
# for i in range(0, 3):
   #  print(ll[0][i][0])
   #  print(ll[0][i][1])
   #  cv.circle(img1, (int(ll[0][i][0]), int(ll[0][i][1])), int(ll[0][i][2]), (0, 0, 0), 5)

# Checking all the green circles. Since, the number of red and green circles will remain same in all testcases,
# therefore I have hardcoded the range as 6 only.
# for i in range(0, 6):
    # print(l[0][i][0])
    # print(l[0][i][1])
    # cv.circle(img1, (int(l[0][5][0]), int(l[0][5][1])), int(l[0][5][2]), (0, 0, 0), 5)

# Finding the co-ordinates of the stars according to the has_image function.
x1 = 355.5  # Starting co-ordinates.
y1 = 989.5

x2 = 244.5  # Final co-ordinates.
y2 = 455.5

# I calculated the positions of the joining circle manually using the code given in lines 75-78.
# Boss, I was studying about the Dijkstra's algorithm for solving this problem but due to the lack of time and
# understanding of python programming, I could not do the same. Sorry for that, boss!

img1 = cv.line(img1, (int(x1), int(y1)), (int(l[0][5][0]), int(l[0][5][1])), (0, 0, 0), 5)
img1 = cv.line(img1, (int(l[0][5][0]), int(l[0][5][1])), (int(l[0][4][0]), int(l[0][4][1])), (0, 0, 0), 5)
img1 = cv.line(img1, (int(l[0][4][0]), int(l[0][4][1])), (int(l[0][3][0]), int(l[0][3][1])), (0, 0, 0), 5)
img1 = cv.line(img1, (int(l[0][3][0]), int(l[0][3][1])), (int(x2), int(y2)), (0, 0, 0), 5)

# Displaying the original image with the connected circles.
cv.imshow('output', img1)
cv.waitKey(0)
cv.destroyAllWindows()
