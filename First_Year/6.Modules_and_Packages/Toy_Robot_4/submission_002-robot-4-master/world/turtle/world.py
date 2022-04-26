import turtle
from world import obstacles as obstacle

# python feature like a drawing a boundary, which lets you command a turtle to draw all over it!
bot = turtle.Turtle()

limit_vars = False

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def show_position(robot_name):
    print(' > '+robot_name+' now at position (' +
          str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, limit_vars
    new_x = position_x
    new_y = position_y
    limit_vars = False

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if obstacle.is_position_blocked(new_x, new_y) or \
    obstacle.is_path_blocked(position_x, position_y, new_x, new_y):
        limit_vars = True
        return False

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global bot, limit_vars
    
    if update_position(steps):
        bot.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif limit_vars == True:
            return True, ''+robot_name+": "+'Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    global bot, limit_vars

    if update_position(-steps):
        bot.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif limit_vars == True:
            return True, ''+robot_name+": "+'Sorry, there is an obstacle in the way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index, bot

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
    bot.right(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index, bot

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
    bot.left(90)
    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """
    global bot

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def boundary_drawing():

    """
    This function illustrate the boundaries/limit areas where robot is not allowed to move beyond them
    """
    bot.penup()  # prevent drawing lines
    bot.speed(0)  # this will make your player created instantly
    #bot.shape("square")  # set player shape
    bot.color("red")  # set player color
    for element in range(2):
        bot.goto(-100, -200)
        bot.pendown()
        bot.goto(-100, 200)
        bot.goto(100, 200)
        bot.goto(100, -200)
        bot.goto(-100, -200)
        bot.penup()
        bot.goto(0, 0)# set player location
        bot.setheading(90)

def obstacles_turtle(obstacle):
    """
    Saves the generated obstacles on save_list and 
    illustrate the obstacles by adding 4 to eitherposition
    """
    global bot
    bot.pencolor("red")
    bot.speed(0)
    for obstacle in obstacle.saved_list:
        bot.fillcolor("red")
        bot.penup()
        bot.goto(obstacle[0], obstacle[1])
        bot.begin_fill()
        bot.pendown()
        bot.goto(obstacle[0], obstacle[1] + 4)
        bot.goto(obstacle[0] + 4, obstacle[1] + 4)
        bot.goto(obstacle[0] + 4, obstacle[1])
        bot.goto(obstacle[0],obstacle[1])


def get_obstacles():
    """
    This function prints a list of object coordinates, that are saved in the obstacles, onto the window.
    """
    obstacles = obstacle.get_obstacles()

    if obstacles:
        print("There are some obstacles:")
        for obst in obstacles:
            
            print("- At position {0},{1} (to {2},{3})".format(str(obst[0]),str(obst[1]),str(obst[0]+ 4),str(obst[1] + 4)))


def show_world():
    """
    Display graphical world with objects and constraints as program starts.
    """
    global position_x, position_y, current_direction_index
    position_x = 0
    position_y = 0
    current_direction_index = 0
    obstacles_turtle(obstacle)
    boundary_drawing()
