import cv2

img = cv2.imread("sanfour.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Image", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
