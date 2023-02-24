def getRealWorld(x_pixel, y_pixel):
    #x = 0.4471x - 423.25
    #y = 5.4878 + 355

    XGRADIENT = 0.445
    XINTERCEPT = -419.2




    YGRADIENT = -0.4487
    YINTERCEPT = 843.55

    # x_pixel = int(input("please enter the x coordinates in pixels"))
    # y_pixel = int(input("please enter the y coordinates in pixels"))
    

    x_world = x_pixel * XGRADIENT + XINTERCEPT
    y_world = y_pixel * YGRADIENT + YINTERCEPT
    # print(f"x-coordinates: {x_world} y-coordinates: {y_world}")
    return x_world, y_world

# while (True):
#     getRealWorld



