import numpy as np
import cv2


src1 = cv2.imread('CHECKPOINT1.png')
x1 = [74, 52, 163]
small = np.array(x1)

x2 = [74, 52, 163]
large = np.array(x2)


masker = cv2.inRange(src1, small, large)
res = cv2.bitwise_and(src1, src1, mask=masker)

cv2.imshow('src1', src1)
cv2.imshow('mask', masker)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
