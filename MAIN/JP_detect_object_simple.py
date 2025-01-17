import cv2

for img_index in range(10,24):
    # Load image
    #image = cv2.imread("MAIN/test/Objects8.png")
    #image = cv2.imread("MAIN/test/Objects"+ str(img_index) +".png")
    image = cv2.imread("MAIN/test/test"+ str(img_index) +".jpg")
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    # Convert to grayscale
    image = cv2.bilateralFilter(image, 45, 95, 95)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(gray, (1, 1), cv2.BORDER_DEFAULT)

    # Find Canny edges
    edged = cv2.Canny(blur, 10 , 200)
    #edged = cv2.GaussianBlur(edged, (5, 5), cv2.BORDER_DEFAULT) # blur the false edges

    # find contours
    contours, hierarchy = cv2.findContours(edged, 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
    
    #cv2.imshow('Canny Edges After Contouring', edged)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # only select closed contour with length < 2000 and length > 20 pixel
    closed_contours = []
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 100 and cv2.arcLength(contours[i], True) < 2000 and cv2.arcLength(contours[i], True) > 20 :
            closed_contours.append(contours[i])

    print("Number of Contours found in Objects" + str(img_index) + " = " + str(len(contours)))
    print("Number of Closed Contours found Objects" + str(img_index) + " = "  + str(len(closed_contours)))

    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(image, closed_contours, -1, (0, 255, 0), 3)

    # Show the image
    cv2.imshow("Detected objects" + str(img_index),image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
