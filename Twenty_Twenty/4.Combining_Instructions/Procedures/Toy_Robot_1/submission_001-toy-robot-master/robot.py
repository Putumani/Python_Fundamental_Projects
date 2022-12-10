

# TODO: Decompose into functions
def move():
    
    square_move(10)
    rectangle_move()
    circle_move()
    dancing_square_move()
    crop_circles_move()
   
def square_move(length):
                                  
    print("Moving in a square of size "+str(length))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
      

def rectangle_move():

    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")

def circle_move():

    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")

def dancing_square_move():

    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        size = 20
        print("* Move Forward "+str(size))
        square_move(size)
            

def crop_circles_move():

    print("Crop circles - 4 circles")
    for i in range(4):
        size = 20
        print("* Move Forward "+str(size))
        circle_move()



def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
