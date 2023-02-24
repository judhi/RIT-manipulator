import socket
from time import sleep
import numpy as np
from getWorldCoordinates import getRealWorld

## Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
## Connect to the EPSON robot
# clientSocket.connect(("192.168.150.2",2001)); # change this according to your robot address
clientSocket.connect(("192.168.150.2",2001)); # this is the EPSON RC7+ simulator on localhost

# format of the coordinate is "x y z u" where u is the wrist rotation angle

# so we will keep the z axis the same and only take values for the x and y values

# places = ["100 400 600 0", "0 500 500 0", "-100 600 400 0"]



def sendToEpson(x, y, robot_z = 850, robot_u = 0):
    coordinates = "JUMP3 " + f"{x} {y} {robot_z} {robot_u}" + "\r\n"
    print (f"Sending to position {x}, {y}")
    clientSocket.send(coordinates.encode())
    confirmation = clientSocket.recv(1023) # waiting for confirmation from robot
    print("result:", confirmation)
    sleep(1)

# while (True):
#     x_pixels = int(input("Please enter the x pixel coordinate value: "))
#     y_pixels = int(input("Please enter the y pixel coordinate value: "))

#     x_robot, y_robot = getRealWorld(x_pixel=x_pixels, y_pixel=y_pixels)
#     sendToEpson(x=x_robot, y=y_robot)
    






# for data in places:
#     # Send data to robot
#     msg_tx = "JUMP3 " + data + "\r\n"
#     print ("Sending: " + msg_tx )
#     clientSocket.send(msg_tx.encode())
#     msg_rx = clientSocket.recv(1023) # waiting for confirmation from robot
#     print("result:", msg_rx)
#     # do something else, like open gripper
#     # then move Z down
#     # close the gripper according to the object size
#     # then jump to the container position
#     # and release the item
#     #etc
#     sleep(1)

clientSocket.close # close the connection