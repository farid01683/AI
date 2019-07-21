import cv2

img = cv2.imread('1.jpg')
img = img[:300, :300]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()