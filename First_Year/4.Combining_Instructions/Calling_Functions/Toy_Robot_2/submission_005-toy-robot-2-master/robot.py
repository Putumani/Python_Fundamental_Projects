add_x, add_y = 0,0

def robot_name():
    """
    prompt a name from a user
    """

    name = input("What do you want to name your robot? ")
    print(f"{name}: Hello kiddo!")
    return name


def get_command(name):
    """
    This function asks for command and check if the given command is valid.
    """

    command = ""
    valid = False

    while not valid:
        command = input(f"{name}: What must I do next? ")
        valid = check_valid_command(name, command)
    return(command.lower())


def check_valid_command(name, command):
    """
    this function checks whether the command is valid or not. 
    """

    commands_list = ["off", "help", "right", "left"]
    command_lower_case = command.lower()

    if "forward" in command_lower_case or "back" in command_lower_case or "sprint" in command_lower_case:
        split_command = command_lower_case.split()
        if len(split_command) > 1:
            steps = split_command[1]
            if steps.isdigit():
                return True
            else:
                invalid_command(name, command)
    if command_lower_case in commands_list:
        return True
    else:
        invalid_command(name, command)


def invalid_command(name, command):
    print(f"{name}: Sorry, I did not understand '{command}'.")
    return False


def command_help():
    """
    prints out help information to the user.
    """

    help_output = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move robot forward a given number of steps
BACK - move robot back a given number of steps
RIGHT - turn the robot 90 degrees to the right
LEFT - turn the robot 90 degrees to the left
SPRINT - sprint forward according to a number of steps"""
    return help_output


def forward_movement(name, new_coordinates,command, direction, num_steps):
    """
    moves the robot forward by the number of steps given with the limits 
    between -200 to 200 for y value and between -100 to 100 for x value
    """
    new_x, new_y = new_coordinates
    num_steps = int(num_steps)
    new_x, new_y = de_incrimenter(name, new_coordinates, command.split()[0], num_steps, direction)
    
    if new_x <= -100 or new_x >= 100 or new_y <= -200 or new_y >= 200:
        return f"{name}: Sorry, I cannot go outside my safe zone."
    else:
        return f" > {name} moved forward by {num_steps} steps."


def track_position(name, coordinates, command, direction,num_steps):
    """ 
    this function gives the position of the robot 
    """

    num_steps = int(num_steps)
    new_coordinates = coordinates
    new_x, new_y = new_coordinates 
    new_x, new_y = de_incrimenter(name,coordinates,command, num_steps, direction)
    
    if new_x <= -100 or new_x >= 100 or new_y <= -200 or new_y >= 200:
        tuple_new_coords = str(tuple(new_coordinates)).replace(' ', '')
        print(f" > {name} now at position {tuple_new_coords}.")
        return new_coordinates
    else:
        if direction == "up":
            new_x, new_y = de_incrimenter(name,coordinates, command, num_steps, direction)
        elif direction == "left":
            new_x, new_y = de_incrimenter(name,coordinates, command, num_steps, direction)
        elif direction == "right":
            new_x, new_y = de_incrimenter(name,coordinates, command,num_steps, direction)
        elif direction == "down":
            new_x, new_y = de_incrimenter(name,coordinates, command,num_steps, direction)
        new_coordinates =  new_x, new_y 
        tuple_new_coords = str(tuple(new_coordinates)).replace(' ', '')
        print(f" > {name} now at position {tuple_new_coords}.")
    return new_coordinates


def de_incrimenter(name,coordinates,command, num_steps, direction):
    """
    when the robot moves forward or backward, this function 
    increase or decrease the y or x value with the number of steps
    """

    new_coordinates = coordinates 
    new_x, new_y = new_coordinates
    num_steps = int(num_steps)

    if "forward" in command.split()[0] or "sprint" in command.split()[0]:
        if direction == "up":
            new_y = new_y + num_steps
        elif direction == "left":
            new_x = new_x - num_steps
        elif direction == "right":
            new_x = new_x + num_steps
        elif direction == "down":
            new_y = new_y - num_steps
    elif "back" in command.split()[0]:
        if direction == "up":
            new_y = new_y - num_steps
        elif direction == "left":
            new_x = new_x + num_steps
        elif direction == "right":
            new_x = new_x - num_steps
        elif direction == "down":
            new_y = new_y + num_steps
    return new_x,new_y


def back_movement(name, new_coordinates, command, direction, num_steps):
    """
    moves the robot back with the number of steps given
    """

    new_x, new_y = new_coordinates
    num_steps = int(num_steps)
    new_x, new_y = de_incrimenter(name, new_coordinates, command.split()[0], num_steps, direction)
    if new_x <= -100 or new_x >= 100 or new_y <= -200 or new_y >= 200:
        return f"{name}: Sorry, I cannot go outside my safe zone."
    else:
        return f" > {name} moved back by {num_steps} steps."
  
        
def sprint_movement(name, new_coordinates, command, direction, num_steps):
    """
    sprints the robot forward with an extra distance
    """

    global add_x, add_y

    new_x, new_y = new_coordinates
    num_steps = int(num_steps)
    new_x, new_y = de_incrimenter(name, new_coordinates, command.split()[0], num_steps, direction)
    add_x += new_x
    add_y += new_y

    if add_x <= -100 or add_x >= 100 or add_y <= -200 or add_y >= 200:
        print(f"{name}: Sorry, I cannot go outside my safe zone.")
        return f" > {name} now at position ({new_x},{new_y})."
    if num_steps == 1:
        print(forward_movement(name, new_coordinates,command, direction, num_steps))
        return f" > {name} now at position ({add_x},{add_y})."
    else:
        print(forward_movement(name, new_coordinates,command, direction, num_steps))
        return sprint_movement(name, new_coordinates, command,direction, int(num_steps) - 1)
    

def turn_right(name):
    return f" > {name} turned right."


def turn_left(name):
    return f" > {name} turned left."


def command_execution(name, command, direction, new_coordinates):
    """
    all movement functions including none-movement functions are executed here
    """

    if command == "off":
        print(f"{name}: Shutting down..")
        return("off")
    elif command == "help":
        print(command_help())
    elif command == "right":
        print(turn_right(name))
        return "right"
    elif command == "left":
        print(turn_left(name))
        return "left"
    elif "forward" in command:
        print(forward_movement(name, new_coordinates,command, direction, command.split()[1]))
        return f"forward;{command.split()[1]}"
    elif "back" in command:
        print(back_movement(name, new_coordinates, command, direction, command.split()[1]))
        return f"back;{command.split()[1]}"
    elif "sprint" in command:
        print(sprint_movement(name, new_coordinates,command, direction, command.split()[1]))


def change_direction(command_name, turn_angles):
    """
    turns the robot to the left or right by 90 degrees
    """

    directions = ["up", "right", "down", "left"]
    num_of_directions = len(directions)
    turn = 0

    if turn_angles == "right":
        turn = 1
    elif turn_angles == "left":
        turn = -1
    current_direction = directions.index(command_name)
    new_direction = current_direction + turn
    if new_direction > num_of_directions - 1:
        new_direction -= num_of_directions
    return directions[new_direction]


def robot_start():
    """This is the entry function, do not change"""
    coordinates = [0, 0]
    initial_position = "up"
    name = robot_name()

    while(True):
        command = get_command(name)
        initialised_command = command_execution(name, command, initial_position, coordinates)
        if initialised_command is not None:
            if initialised_command == "off":
                break
            elif ";" in initialised_command:
                coordinates = track_position(name, coordinates, initialised_command, initial_position,command.split()[1])
            else:
                initial_position = change_direction(initial_position, initialised_command)
                tuple_coordinates = str(tuple(coordinates)).replace(' ', '')
                print(f" > {name} now at position {tuple_coordinates}.")


if __name__ == "__main__":
    robot_start()
