import cv2

# Load image
image = cv2.imread("MAIN/test/Objects2.png")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce noise
blur = cv2.GaussianBlur(gray, (1, 1), 0)
cv2.imshow("blur",blur)
cv2.waitKey(0)

# Find circles
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 10, minRadius=5, maxRadius=200)

# Draw circles on the image
if circles is not None:
    circles = circles[0]
    for circle in circles:
        x, y, r = circle.astype(int)
        cv2.circle(image, (x, y), r, (0, 0, 255), 2)
        print("Drawing")
else:
    print("No circles found")

# Find rectangles
contours, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles on the image
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    if len(approx) == 4:
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

# Show the image
cv2.imshow("Gray",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
