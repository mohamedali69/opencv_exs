import cv2

backgroundSubtractor = cv2.createBackgroundSubtractorMOG2()

img1 = cv2.imread("sanfour1.jpg")
img2 = cv2.imread("sanfour2.jpg")

fgmask1 = backgroundSubtractor.apply(img1)

contours, hierarchy = cv2.findContours(
    fgmask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image_contour = cv2.drawContours(img1, contours, -1, (0, 255, 0), 2)

cv2.imshow("Contours", image_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
