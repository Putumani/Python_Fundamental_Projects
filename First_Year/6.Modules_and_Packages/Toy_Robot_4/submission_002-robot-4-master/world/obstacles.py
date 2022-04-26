import random


save_list = []

x_values = bool
y_values = bool


def generate_saved_list():
    """
    Generates the obstacles from a range of
    interger values (0 to 10) 
    and within the min_y,max_y
    to min_x,max_x values
    and append them to  
    an empty save_list
    """
    global save_list
    

    randomnumber = random.randint(0, 10)
    
    for element in range(randomnumber):
        x = (random.randint(-100,100))
        y = (random.randint(-200,200))

        save_list.append([x,y])
    return save_list

 
def is_position_blocked(x, y):
    """
    Checks if the is any position blocked 
    """
    global save_list

    for obstacle in save_list:
        if x >= obstacle[0] and x <= (obstacle[0] + 4) and y >= obstacle[1] and y <= (obstacle[1] + 4):
            return True 
        else:
            return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks if there is any path blocked
    """
    global save_list,x_values,y_values

    while True:
        for x in save_list:
            if y1 == y2:
                for i in range(x[1], x[1] + 4):
                    if i == y1:
                        x_values = True

                for i in range(min([x1, x2]),max([x1, x2]) + 1):
                    if i >= x[0] and i <= x[0] + 4:
                        y_values = True

            elif x_values == True:
                if  y_values == True:
                    return True

            if x1 == x2:
                for i in range(x[0], x[0] + 4):
                    if i == x1:
                        x_values = True

                for i in range(min([y1, y2]), max([y1, y2]) + 1):
                    if i >= x[1] and i <= x[1] + 4:
                        y_values = True
                        
            elif x_values == True:
                if  y_values == True:
                    return True

        return False
        break


def get_obstacles():
    global save_list
    save_list = generate_saved_list()
    return save_list