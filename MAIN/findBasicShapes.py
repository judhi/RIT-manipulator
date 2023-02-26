import cv2

# Load image
image = cv2.imread("MAIN/test/Objects7.png")
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Convert to grayscale
image = cv2.bilateralFilter(image, 45, 95, 95)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Blur the image to reduce noise
blur = cv2.GaussianBlur(gray, (1, 1), cv2.BORDER_DEFAULT)

# Find Canny edges
edged = cv2.Canny(blur, 10 , 200)
edged = cv2.GaussianBlur(edged, (5, 5), cv2.BORDER_DEFAULT)
#ret, edged = cv2.threshold(edged, 200, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow("blur",blur)
#cv2.waitKey(0)

# # Find circles
# circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1,5, param2=95, minRadius=5, maxRadius=900)

# # Draw circles on the image
# if circles is not None:
#     circles = circles[0]
#     for circle in circles:
#         x, y, r = circle.astype(int)
#         cv2.circle(image, (x, y), r, (0, 0, 255), 2)
#         print("Drawing")
# else:
#     print("No circles found")

# Find rectangles
# contours, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Draw rectangles on the image
# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
#     if len(approx) == 4:
#         cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

closed_contours = []
 
for i in range(len(contours)):
    #if cv2.contourArea(contours[i]) > cv2.arcLength(contours[i], True):
    if cv2.contourArea(contours[i]) > 130 and cv2.arcLength(contours[i], False) < 2000 and cv2.arcLength(contours[i], False) > 0 :
    #if cv2.contourArea(contours[i]) > 130 and cv2.arcLength(contours[i], True) < 2000:
        closed_contours.append(contours[i])

print("Number of Contours found = " + str(len(contours)))
print("Number of Closed Contours found = " + str(len(closed_contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, closed_contours, -1, (0, 255, 0), 3)
# for i in range(len(closed_contours)):
#     print(i," ",cv2.arcLength(closed_contours[i], True))
#     cv2.drawContours(image, closed_contours[i], -1, (0, 255, 0), 3)

# Show the image
cv2.imshow("Detected",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
