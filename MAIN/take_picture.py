import cv2
# import keyboard

camera = cv2.VideoCapture(0)
count = 0

while(True):
    ret, frame = camera.read()
    if ret:
        cv2.imshow("table", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            count += 1
            print("Take a picture")
            cv2.imwrite(f"{count}.png", frame)
            #break

    # if keyboard.is_pressed("a"):
    #     count += 1
    #     print("Take a picture")
    #     cv2.imwrite(f"{count}.png", frame)

camera.release()
# Destroy all the windows
cv2.destroyAllWindows()