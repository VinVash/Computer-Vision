import cv2 as cv
import numpy as np


# If this program cannot be made using loop, then submit the checkpoint3_copy.jpg image along with.
# If this program can be looped, then no need to submit the image checkpoint3_copy.jpg.
# In either case, you have to submit the image checkpoint3star.jpg.

# Writing a program to detect needle in a haystack, i.e., detecting the smaller picture in the bigger one.


def has_image(haystack, needle):
    haystack = cv.cvtColor(haystack, cv.COLOR_BGR2GRAY)
    needle = cv.cvtColor(needle, cv.COLOR_BGR2GRAY)
    w, h = needle.shape[::-1]  # width and height of the small image is saved in 'w' and 'h' respectively.
    res = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)
    threshold = 0.80  # setting the threshold to 80% accuracy. This way it determines the star located at Chennai too.
    loc = np.where(res >= threshold)
    try:
        assert loc[0][0] > 0
        assert loc[1][0] > 0
        return loc[1][0] + w / 2, loc[0][0] + h / 2  # Return the co-ordinates of the center of the smaller image in the
        # bigger one.
    except:
        return -1, -1  # Else return some proof that the smaller image is not present in the bigger image.


if __name__ == "__main__":
    bigger = cv.imread('checkpoint3.jpg')  # First read the image checkpoint 3 in the bigger variable so that it returns
    # the co-ordinates of the first occurrence of the image. Then, comment this line and uncomment the next one.

    # bigger = cv.imread("checkpoint3_copy.jpg")
    # Sorry, but I could not find a way out through a loop, but we have to
    # erase the first detected occurrence of the star and then save it in the variable, checkpoint3_copy.jpg through
    # which the second occurrence of the star is detected.
    smaller = cv.imread("checkpoint3star.jpg")

    x, y = has_image(bigger, smaller)

    if x >= 0 and y >= 0:
        print(x)
        print(y)
        w, h, _ = smaller.shape
        cv.imshow("Found the smaller at (%d,%d)" % (x, y), bigger)
        cv.waitKey(0xFFFF)
    else:
        print("Not found")

# By this file, we have the co-ordinates of the stars in the map. Now, the co-ordinates of Jaipur will always remian
# same in every testcase, i.e. (244.5, 455.5) and the start co-ordinates will differ only.
