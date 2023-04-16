import cv2

backgroundSubtractor = cv2.createBackgroundSubtractorMOG2()

img1 = cv2.imread("sanfour1.jpg")
img2 = cv2.imread("sanfour2.jpg")

fgmask1 = backgroundSubtractor.apply(img1)
fgmask2 = backgroundSubtractor.apply(img2)

# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
# gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)

mse = ((fgmask1 - fgmask2) ** 2).mean()

imgout = fgmask1 - fgmask2

print("MSE:", mse)
cv2.imshow("Difference Image", imgout)

cv2.waitKey(0)
cv2.destroyAllWindows()
